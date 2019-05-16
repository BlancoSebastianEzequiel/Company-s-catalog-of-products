class Auth {
  setApp (app) {
    this.app = app
  }

  getToken () {
    if (!this.token) {
      this.token = sessionStorage.getItem('auth')
    }
    return this.token
  }

  isLogged () {
    return this.getToken() !== null
  }

  login (token) {
    sessionStorage.setItem('auth', token)
  }

  logout (callback) {
    this.token = null
    sessionStorage.clear()
    if (callback) {
      callback()
    } else {
      alert('Your session has been closed')
    }
    if (this.app) {
      this.app.forceUpdate() // Hack to redirect to login
    }
  }
}
const instance = new Auth()
export default instance
