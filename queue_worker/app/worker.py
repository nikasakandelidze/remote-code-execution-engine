from celery import Celery
from adapter.fileSystemAdapter import write_content_in_random_file

import subprocess, os

celery = Celery("code_execution_worker")
celery.conf.broker_url="amqp://guest:guest@mqueue:5672/"
celery.conf.result_backend="redis://redis:6379"


cli_runtime_for_language = {
    "python":"python",
    "javascript": "node"
}


@celery.task(name="execute_code_task")
def execute_code(code, language):
    print(f"Inputs of queue worker. Code: {code}, language: {language}")
    file_name = write_content_in_random_file(code, language)
    try:
        print(f"Name of the file created for worker to execute is: {file_name}.")
        command = cli_runtime_for_language[language.lower()]
        process = subprocess.Popen([command, file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if err:
            res = err.decode("utf-8")
            print(f"error here: {res}")
            return {"status": res}
        else:
            res = out.decode("utf-8")
            print(f"Successfully executed file with code. Returning result: {res}.")
            return {"output": res, "status": "good"}
    except Exception as e:
        print(e)
        return {"status": e}
    finally:
        if file_name:
            os.remove(file_name)