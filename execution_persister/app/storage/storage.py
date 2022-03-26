from sqlalchemy.orm import Session
from storage.entity import Code,Language


class Storage:
    def __init__(self):
        pass

    def get_all_executed_codes(self, db: Session):
        return db.query(Code).all()


    def get_all_languages(self, db: Session):
        return db.query(Language).all()


    def get_language_with_title(self, db: Session, name: str):
        return db.query(Language).filter(Language.name == name).first()


    def insert_new_code(self, db: Session, language: str, code:str):
        lang = self.insert_new_language(db, language)
        new_code = Code(code_input=code, language_id=lang.id)
        db.add(new_code)
        db.commit()
        db.refresh(new_code)
        return new_code


    def insert_new_language(self, db: Session, language: str):
        search_result = self.get_language_with_title(db, language)
        if search_result:
            return search_result
        new_language = Language(name=language)
        db.add(new_language)
        db.commit()
        db.refresh(new_language)
        return new_language