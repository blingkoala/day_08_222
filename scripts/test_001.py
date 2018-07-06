import allure
class Test_001:
    @allure.step(title = "第一个测试")
    def test_001(self):
        allure.attach("描述", "描述内容")

        assert 0