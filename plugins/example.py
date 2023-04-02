from apisix.runner.plugin.base import Base
from apisix.runner.http.request import Request
from apisix.runner.http.response import Response


class Stop(Base):
    def __init__(self):
        """
        Example of `stop` type plugin, features:
            This type of plugin can customize response `body`, `header`, `http_code`
            This type of plugin will interrupt the request
        """
        super(Stop, self).__init__(self.__class__.__name__)

    def filter(self, request: Request, response: Response):
        """
        The plugin executes the main function
        :param request:
            request parameters and information
        :param response:
            response parameters and information
        :return:
        """
        # 在插件中可以通过 `self.config` 获取配置信息，如果插件配置为JSON将自动转换为字典结构
        # print(self.config)

        # 设置响应头信息
        headers = request.headers
        headers["X-Resp-A6-Runner"] = "Python"
        response.headers = headers

        # 设置响应体信息
        response.body = "Hello, Python Runner of APISIX"

        # 设置响应状态码
        response.status_code = 201

        # 通过调用 `self.stop()` 中断请求流程，此时将立即响应请求给客户端
        # 如果未显示调用 `self.stop()` 或 显示调用 `self.rewrite()`将继续将请求
        # 默认为 `self.rewrite()`
        self.stop()
