import Auth from '../service/Auth'
import httpStatus from 'http-status-codes'

class Http {
  async get (url, callback) {
    const rawResponse = await fetch(url, {
      method: 'GET',
      headers: this.getHeaders()
    })
    this.checkIfUnauthorized(rawResponse.status, callback)
    const content = await rawResponse.json()
    return {
      content,
      status: rawResponse.status
    }
  }

  async delete (url, id, callback) {
    const rawResponse = await fetch(`${url}${id}/`, { method: 'DELETE', headers: this.getHeaders() })
    this.checkIfUnauthorized(rawResponse.status, callback)
    const content = await rawResponse.json()
    return {
      content,
      status: rawResponse.status
    }
  }

  async post (url, payload, callback) {
    const rawResponse = await fetch(url, {
      method: 'POST',
      headers: this.getHeaders(),
      body: JSON.stringify(payload)
    })
    this.checkIfUnauthorized(rawResponse.status, callback)
    const content = await rawResponse.json()
    return {
      content,
      status: rawResponse.status
    }
  }

  async patch (url, payload, callback) {
    const rawResponse = await fetch(url, {
      method: 'PATCH',
      headers: this.getHeaders(),
      body: JSON.stringify(payload)
    })
    this.checkIfUnauthorized(rawResponse.status, callback)
    const content = await rawResponse.json()
    return {
      content,
      status: rawResponse.status
    }
  }

  checkIfUnauthorized (status, callback) {
    if (status === httpStatus.UNAUTHORIZED) {
      Auth.logout(callback)
    }
  }

  getHeaders () {
    let headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    }
    if (Auth.isLogged()) {
      headers['Authorization'] = 'Bearer ' + Auth.getToken()
    }
    return headers
  }
}
const instance = new Http()
export default instance
