import src.pydanticModels as pydanticModels
import src.laureatePydanticModel as laureateModels
import json
from flask import Response, request
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
import src.apiRequest as apiRequest
from src.params import NobelParams, LaureateParams
from datetime import date

info = Info(title="API Prêmio nobel", version="1.0.0", description="API de conexão externa a API de prêmio nobel")
app = OpenAPI(
    __name__,
    info=info,
    servers=[]   
)
CORS(app)

nobel_tag = Tag(name="Nobel", description="Operações relacionadas a Nobel")


@app.get(
    "/exactSciences",
    tags=[nobel_tag],
    responses={
        200: pydanticModels.NobelResponse,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse,
    }
)
def get_science_nobels():
    """Retorna os prêmios nobels de ciências exatas da ultima decada."""
    try:
        current_year = date.today().year
        params = NobelParams(
        sort ="asc",
        nobelPrizeCategory = "che",
        nobelPrizeYear = current_year - 10,
        yearTo = current_year
            )
        nobelsche, status = apiRequest.nobel(params)
        if status == 200:
            params.nobelPrizeCategory = "phy"
            nobelsPhy, status = apiRequest.nobel(params)
            nobels = {**nobelsche, **nobelsPhy}
        parsed = pydanticModels.NobelResponse(**nobels)
            
        if not parsed:
            return Response(
                json.dumps({"message": "Nenhum Prêmio encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(parsed.model_dump(), ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar Nobels: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json"
        )
    
@app.get(
    "/nobelByCategory",
    tags=[nobel_tag],
    responses={
        200: pydanticModels.NobelPrize,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def get_nobels_by_category(query: pydanticModels.CategoryQuery):
    """Retorna os prêmios nobels por categoria e ano"""
    try:
        nobels, status = apiRequest.nobelByCategory(query.category, query.year)
        parsed = pydanticModels.NobelPrize(**nobels[0])
        if not nobels:
            return Response(
                json.dumps({"message": "Nenhum Prêmio encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(parsed.model_dump(), ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar Nobels: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json")
    
@app.get(
    "/laureates",
    tags=[nobel_tag],
    responses={
        200: laureateModels.LaureateResponse,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def get_laureates():
    """Retorna os ganhadores do prêmio nobel na ultima decada"""
    try:
        current_year = date.today().year
        params = LaureateParams(
            nobelPrizeYear = current_year - 10,
            yearTo = current_year
        )
        laureates, status = apiRequest.laureates(params)

        if not laureates:
            return Response(
                json.dumps({"message": "Nenhum ganhador encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(laureates, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar ganhadores: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json")
@app.get(
    "/laureatesById",
    tags=[nobel_tag],
    responses={
        200: laureateModels.LaureateIdResponse,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)
def get_laureates_by_id(query: pydanticModels.LaureateQuery):
    """Retorna os ganhadores do prêmio nobel pelo ID"""
    try:
        laureate, status = apiRequest.laureatesById(query.id)

        if not laureate:
            return Response(
                json.dumps({"message": "Nenhum ganhador encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(laureate, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar ganhadores: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json")

@app.get(
    "/laureatesByIds",
    tags=[nobel_tag],
    responses={
        200: laureateModels.LaureateIdsResponse,
        404: pydanticModels.DefaultResponse,
        500: pydanticModels.DefaultResponse
    }
)

def get_laureate_by_ids(query: pydanticModels.LaureateParams):
    """Retorna mutiplos ganhadores por ids"""
    try:
        data = []
        ids = request.args.getlist("ids") 
        for id in ids:
            laureate, status = apiRequest.laureatesById(id)
            laureate = laureateModels.LaureateIdResponse(**laureate)
            data.append(laureate.model_dump())

        if not data:
            return Response(
                json.dumps({"message": "Nenhum ganhador encontrado"}, ensure_ascii=False),
                status=404,
                mimetype="application/json"
            )
        return Response(
            json.dumps(data, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    except Exception as e:
        return Response(
            json.dumps({"message": f"Erro ao buscar ganhadores: {str(e)}"}, ensure_ascii=False),
            status=500,
            mimetype="application/json")            
    
    
if __name__ == "__main__":
    app.run()
