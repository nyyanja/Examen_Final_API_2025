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
    return {"identifier": "",
            "brand": "",
            "model": "",
            "characteristics": {"max-speed": "",
                                "max_fuel_capacity": ""},200}



