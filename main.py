from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"pong"}


@app.post("/cars")
def car_list():
    identifiers  = [""]
    brands = [""]
    models = [""]
    characteristics = [{"max-speed": "",
                        "max_fuel_capacity": ""}]
    return {{"identifiers": identifiers,
            "brands": brands,
            "models": models,
            "characteristics": characteristics},201}
@app.get("/cars")
def car_list():
    identifiers  = [""]
    brands = [""]
    models = [""]
    characteristics = [{"max-speed": "",
                        "max_fuel_capacity": ""}]
    return {{"identifiers": identifiers,
            "brands": brands,
            "models": models,
            "characteristics": characteristics},200}
@app.get("/cars/{id}")
def car_detail(id: int):
    if id  not in car_list():
        return {"error": "Car not found"},404

@app.put("/cars/{id}/characteristics")
def update_car_characteristics(id: int, max_speed: int, max_fuel_capacity: int):
    if id  not in car_list():
        return {"error": "Car not found"},404
    if max_speed <= 0 or max_fuel_capacity <= 0:
        return {"error": "Invalid characteristics"},400
    return {"id": id,
            "max_speed": max_speed,
            "max_fuel_capacity": max_fuel_capacity},200



