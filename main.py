from fastapi import FastAPI

app = FastAPI()

@app.get("/phone-brand/{phone_id}")
def get_phone_brand(phone_id: int):
    phone_brands = {
        1: "Apple",
        2: "Samsung",
        3: "Google",
        4: "OnePlus",
        5: "Xiaomi"
    }
    return {"phone_id": phone_id, "phone_brand": phone_brands.get(phone_id, "Unknown brand")}
