from fastapi import HTTPException


class AppException(HTTPException):
    """애플리케이션 기본 예외"""

    def __init__(self, code: str, message: str, status_code: int = 400):
        self.code = code
        self.message = message
        super().__init__(status_code=status_code, detail={"code": code, "message": message})


class NotFoundException(AppException):
    """리소스를 찾을 수 없음"""

    def __init__(self, message: str = "리소스를 찾을 수 없습니다"):
        super().__init__("NOT_FOUND", message, 404)


class BadRequestException(AppException):
    """잘못된 요청"""

    def __init__(self, message: str = "잘못된 요청입니다"):
        super().__init__("BAD_REQUEST", message, 400)


class ValidationException(AppException):
    """유효성 검사 실패"""

    def __init__(self, message: str = "유효성 검사에 실패했습니다", details: dict = None):
        super().__init__("VALIDATION_ERROR", message, 422)
        self.details = details
