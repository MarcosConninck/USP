from fastapi import APIRouter, Depends, status, HTTPException
import esquemas, repositorio, modelos
from banco_de_dados import obter_sessao
from configuracao import logger
from sqlalchemy.orm import Session
import traceback
from oath2 import obter_usuario_atual

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

# METODO POST (CRIAR UM RECURSO)
# ENDPOINT (http://localhost:8000/usuarios/)
@router.post("/", response_model=esquemas.UsuarioResposta, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario:esquemas.UsuarioCriacao, db: Session = Depends(obter_sessao)):
    try:
        novo_usuario = repositorio.criar_usuario(db,usuario)
        logger.info(f"Usuário criado com sucesso: {novo_usuario.nome} (ID: {novo_usuario.id})")
        return novo_usuario
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Erro na criação do usuário.")
    
# METEDO GET (OBTER RECURSO)
# ENDPOINT (http://localhost:8000/usuarios/{usuario_id})
@router.get("/{usuario_id}", response_model=esquemas.UsuarioResposta)
def obter_usuario(usuario_id:int, db: Session = Depends(obter_sessao)):
    try:
        usuario =  repositorio.obter_usuario_por_id(db, usuario_id)
        return esquemas.UsuarioResposta(
            id=usuario.id,
            nome=usuario.nome,
            email=usuario.email
        )
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não encontrado.")
        
@router.get("/")
def listar_usuarios(db: Session = Depends(obter_sessao)):
    try:
        usuarios = repositorio.obter_usuarios(db)
        return [
            esquemas.UsuarioResposta(
                id=usuario.id,
                nome=usuario.nome,
                email=usuario.email
            ) for usuario in usuarios
        ]
    except Exception as e:
        traceback.print_exc()
        logger.error(e)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuários não encontrados")

@router.get("/meus_dados")
def meus_dados(usuario_atual: modelos.Usuario = Depends(obter_usuario_atual))