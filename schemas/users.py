from pydantic import BaseModel

class Creds(BaseModel):
  email: str
  password: str

class Token(BaseModel):
  token: str
  expires: int

class TokenAuth(BaseModel):
  token: str

class User(BaseModel):
  id: str # User ID
  token: Token # User token info (token, token expires (number of milliseconds from 1970))
  auth: Creds # User credentaials (email, password)
  username: str # User username
  photo: str # User photo (base64)
  role: str # User role (author/user)
  code: str # Code, that sended to user's email

class UserProfile(BaseModel):
  id: str
  email: str
  username: str
  photo: str

class RegisterUser(BaseModel):
  auth: Creds
  check_password: str

class LoginUser(BaseModel):
  auth: Creds
  token_auth: TokenAuth

class LoginUserProfile(BaseModel):
  id: str
  email: str
  username: str
  photo: str
  token: str

class CheckCode(BaseModel):
  email: str
  code: str

class NewPassword(BaseModel):
  new_password: str
  check_new_password: str

class SetNewPassword(BaseModel):
  email: str
  code: str
  new_password: NewPassword

class ChangeUserUsername(BaseModel):
  username: str
  user: TokenAuth

class ChangeUserEmail(BaseModel):
  email: str
  user: TokenAuth

class ChangeUserPassword(BaseModel):
  old_password: str
  new_password: NewPassword
  user: TokenAuth

class ChangeUserPhoto(BaseModel):
  photo: str
  user: TokenAuth

class ChangeUserRole(BaseModel):
  id: str
  role: str
  admin: TokenAuth

class DeleteUser(BaseModel):
  id: str
  user: TokenAuth