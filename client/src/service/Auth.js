class Auth {
  constructor (type) {
    this.type = null
  }

  setApp (app) {
    this.app = app
  }

  getToken () {
    if (!this.token) {
      this.token = sessionStorage.getItem('auth')
    }
    return this.token
  }

  setTypeOfUser (type) {
    this.type = type
  }

  isAdmin () {
    if (!this.type) {
      return true
    }
    return this.type === 'admin'
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
