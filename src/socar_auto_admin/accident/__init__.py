from flask import Blueprint

accident_blueprint = Blueprint(
    "accident", __name__,
    url_prefix="/accident",
    template_folder="templates/accident"
)

from . import views  # 블루프린트에 라우팅 등록
