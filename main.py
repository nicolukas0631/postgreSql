from fastapi import FastAPI, Response
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

@app.get("/, status_code=HTTP_200_OK)")
def root():
    items = []
    for data in conn.read_all():
        dict_data = {}
        dict_data["id"] = data[0]
        dict_data["username"] = data[1]
        dict_data["phone"] = data[2]
        items.append(dict_data)
    return items

@app.get("/api/user/{id}, status_code=HTTP_200_OK)")
def get_user(id: int):
    data = conn.read_by_id(id)
    if data:
        return {
            "id": data[0],
            "username": data[1],
            "phone": data[2]
        }
    return {"error": "User not found"}, 404

@app.post("/api/insert, status_code=HTTP_201_CREATED)")
def insert_user(user_data: UserSchema):
    data = user_data.dict()
    data.pop("id")
    print(data)
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)


@app.put("/api/update/{id}, status_code=HTTP_204_NO_CONTENT)")
def update_user(id: int, user_data: UserSchema):
    data = user_data.dict()
    data["id"] = id
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)


@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(id: int):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)