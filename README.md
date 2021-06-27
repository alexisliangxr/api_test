说明：
本框架是为了快速实现http/https协议而设计的一套数据驱动自动化接口框架,基于request+unittest设计,pytest作为执行器,本框架在后续的使用中需自己编写测试用例，登入的token等之类的接口已经封装完毕。接口用例编写,接口关联,接口断言可持续添加。
Description:
This framework is a set of data-driven automation interface framework designed for the rapid implementation of HTTP / HTTPS protocol. It is designed based on request + unittest, and pytest is used as the executor. In the subsequent use of this framework, you need to write your own test cases, and the login token and other interfaces have been encapsulated. Interface case writing, Interface Association, interface assertion adding.

环境部署：
解压压缩包api_code.tar.gz，使用vscode打开项目文件
安装python3，pytest即可使用
Environment deployment:
Decompression package api_code.tar.gz, use vscode to open the project file.
Install python3, pytest can be used.


目录说明：
apitest目录下是封装好的获取request，生成token等函数
tests目录下是针对api test pdf中相关需测内容的测试用例
注：api中被测字段众多，以pdf中Payload fields内容为主，其余字段后续可继续添加测试用例
Description of contents:
The apitest directory contains encapsulated functions such as obtaining request and generating token.
In the tests directory, there are test cases for the content to be tested in API test PDF.
Note: There are many fields to be tested in the API, mainly the content of payload fields in PDF, and other fields can continue to add test cases later.

如何执行自动化测试：
How to perform automated testing:
pytest ./tests/test_XXX.py
