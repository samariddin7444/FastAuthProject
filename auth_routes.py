import _datetime
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy import or_
from database import SessionLocal,engine
from schemas import SignUp
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi import status


auth_router = APIRouter(
    prefix="/auth",
)

@auth_router.get("/")
async def auth_(Authorize: AuthJWT= Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": " Hi auth"}

@auth_router.get("/signup")
async def auth_():
    return {"message": " Hi auth"}

@auth_router.post('/signup',status_code=status.HTTP_201_CREATED)
async def signup(user : SignUp):
    session = SessionLocal() # create a new session instance

    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return {'message': 'Email already registered!', 'status_code': status.HTTP_400_BAD_REQUEST}
    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return {'message': 'Username already registered!'}
    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff

    )
    session.add(new_user)
    session.commit()
    user data={
        'username': user.username,
        'email': user.email,
        'is_active': user.is_active,
        'is_staff': user.is_staff,
    }
    return {'massage': 'User created succesfully','new_user': user_data, 'status_code': status.HTTP_201_CREATED}

@auth_router.post('/login',status_code=status.HTTP_201_CREATED)
async def login(user : SignUp, Authorize: AuthJWT=Depends()):
    session = SessionLocal()
    db_email = session.query(User).filter(or_(
        User.username == user.username_or_email,
        User.email == user.username_or_email,
        )
    ).first()

    if db_user and check_password_hash(db_email.password, user.password):
        access_lifetime = datatime.timedelta(minutes=30)
        refresh_lifetime = datatime.timedelta(days=3)
        access_token = Authorize.create_access_token(subject=user.username, expires_delta=access_lifetime)
        refresh_token = Authorize.create_refresh_token(subject=db_user_username,expires_time=refresh_lifetime)
        token = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        responce_data = {
            'status': status.HTTP_200_OK,
            'message': 'Successfully logged in!',
            'token': token
        }
        return responce_data
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Invalid credentials")