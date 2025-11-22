"""
定义应用程序级别的异常
"""
from typing import Optional
class DomainException(Exception):
    """
    领域异常基类
    """
    def __init__(self, message: str, code: Optional[int] = None):
        super().__init__(message)
        self.message = message
        self.code = code
class AuthenticationException(DomainException):
    """
    认证异常
    """
    def __init__(self, message: str = "认证失败", code: Optional[int] = None):
        super().__init__(message, code)
class DuplicateResourceException(DomainException):
    """
    资源重复异常
    """
    def __init__(self, message: str = "数据已存在", code: Optional[int] = None):
        super().__init__(message, code)
class NotFoundException(DomainException):
    """
    资源未找到异常
    """
    def __init__(self, message: str = "数据不存在", code: Optional[int] = None):
        super().__init__(message, code)
class ValidationException(DomainException):
    """
    验证异常
    """
    def __init__(self, message: str = "数据验证失败", code: Optional[int] = None):
        super().__init__(message, code)