from fastapi import APIRouter, Request
from config.dbdapot import dapot_connection
from config.dbdkr import dkr_connection
from config.dbfull import sch_connection
from schemas.schools import SchoolPadalarang, SchoolsPadalarang
from models.schools import School
from bson import ObjectId
import pymongo

sch = APIRouter(tags=["Schools"])

@sch.get('/')
async def find_all_schools():
    school_cursor = sch_connection.local.school.find()
    school_list = list(school_cursor)
    if not school_list:
        return "Data not Found"
    result = [SchoolPadalarang(school) for school in school_list]
    return result

@sch.post('/')
async def create_schools(school : School):
    sch_connection.local.school.insert_one(dict(school))
    return SchoolsPadalarang(sch_connection.local.school.find())

@sch.put('/{id}')
async def update_school(id, school: School):
    updated_school = sch_connection.local.school.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(school)},
        return_document=pymongo.ReturnDocument.AFTER
    )
    return SchoolPadalarang(updated_school)

@sch.delete('/{id}')
async def delete_school(id):
    school = sch_connection.local.school.find_one_and_delete({"_id": ObjectId(id)})
    if school:
        return SchoolPadalarang(school)
    else:
        return {"message": "Data not found"}
