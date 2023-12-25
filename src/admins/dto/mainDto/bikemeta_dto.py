from pydantic import BaseModel,constr,validator,ValidationError

class BikeMetaDTO(BaseModel):
    asking_price:constr(min_length=1,max_length=10,strip_whitespace=True)
    year_of_model:constr(min_length=1,max_length=10,strip_whitespace=True)
    engine_cc:constr(min_length=1,max_length=10,strip_whitespace=True)
    engine_type:constr(min_length=1,max_length=50,strip_whitespace=True)
    kms_run:constr(min_length=1,max_length=50,strip_whitespace=True)
    no_of_owners:constr(min_length=1,max_length=50,strip_whitespace=True)
    available:constr(min_length=1,max_length=50,strip_whitespace=True)
    mileage:constr(min_length=1,max_length=50,strip_whitespace=True)
    buy_year:constr(min_length=1,max_length=10,strip_whitespace=True)
    color:constr(min_length=1,max_length=50,strip_whitespace=True)
    details:constr(min_length=1,strip_whitespace=True)