from fastapi_blocks import BlockSettingsMixin, BlockManager
from sqlmodel import Session, select
from .schemas import SomeData

def insert_test_data(*args, **kwargs):
    bm = BlockManager()
    engine = bm.get_db_engine() # Will raise error if not engine
    
    with Session(engine) as session:
        stmt = select(SomeData).limit(1)
        result = session.exec(stmt).first()
        
        if not result:
            session.add(SomeData(content="Hello World"))
            session.add(SomeData(content="Hello World2"))
            session.add(SomeData(content="Hello World3"))
            session.commit()

class Settings(BlockSettingsMixin):
    
    def _start_hooks(self):
        return super()._start_hooks() + [insert_test_data]