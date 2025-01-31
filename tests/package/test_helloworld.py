from package.helloworld import HelloWorld# test_hello_world.py

def test_hello_world_method():
    # 创建HelloWorld类的实例
    hello = HelloWorld()
    
    # 调用HelloWorld方法并断言返回值
    assert hello.HelloWorld() == "Hello World!"