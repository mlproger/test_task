from fastapi import APIRouter
from fastui import components as c, prebuilt_html, FastUI


router = APIRouter(tags=["Greeting"])


@router.get("/", response_model=FastUI, response_model_exclude_none=True)
async def greet(name: str = "Recruto", message: str = "Давай дружить"):
    return c.Page(components= [
        c.Heading(
            text = f"Hello {name}! {message}!",
            class_name="position-absolute start-50 translate-middle"
        )
    ])