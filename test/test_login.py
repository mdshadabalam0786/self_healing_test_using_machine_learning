from pages.login import Login
def test_login(launch_browser):
    p1=Login(launch_browser)
    p1.loginWithValidCredential()