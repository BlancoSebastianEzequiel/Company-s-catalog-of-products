import React from 'react'
import { Redirect } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'
import ListForm from '../components/ListForm'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class DeleteClientContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      errors: {},
      refresh: false,
      clients: [{
        'data': '',
        '_id': ''
      }],
      redirectTo: false,
      urlToRedirect: '/modify-client',
      dataToRedirect: {}
    }
  }

  handleChange = (name, value) => {
    this.setState({
      [name]: value
    })
  }

  getClients = () => {
    if (this.state.refresh) return
    let clientsVector = []
    Http.get('/users/?type=client')
      .then(response => {
        if (response.status === httpStatus.OK) {
          const length = response.content.data.length
          for (let i = 0; i < length; i++) {
            const aClient = response.content.data[i]
            const _id = response.content.data[i]._id
            clientsVector.push(
              {
                'data': 'USER NAME: ' + aClient['user_name'] + ' -- EMAIL: ' + aClient['email'],
                '_id': _id
              })
          }
          this.handleChange('clients', clientsVector)
          this.handleChange('refresh', false)
        } else {
          toast('ERROR: ' + response.content.data)
        }
      })
      .catch(err => {
        toast('ERROR: ' + err)
      })
  }

  modifyClient = (aClient) => {
    this.setState({ redirectTo: true })
    this.setState({ dataToRedirect: aClient })
  }

  deleteClient = (aClient) => {
    Http.delete('/users/', aClient._id)
      .then(response => {
        if (response.status === httpStatus.OK) {
          this.setState({ 'refresh': true })
          toast('The deletion succeed')
        } else {
          toast('The deletion did not succeed: ' + response.content.data)
        }
      })
      .catch(err => {
        toast('ERROR: ' + err)
      })
  }

  render () {
    const { errors, clients, redirectTo, urlToRedirect, dataToRedirect } = this.state
    if (redirectTo) {
      return <Redirect to={{
        pathname: urlToRedirect,
        state: { id: dataToRedirect._id }
      }}
      />
    }
    return (
      <div>
        <ToastContainer></ToastContainer>
        <ListForm
          errors={errors}
          ObjectsList={clients}
          getList={() => this.getClients()}
          deleteObject={(aClient => this.deleteClient(aClient))}
          modifyObject={(aClient) => this.modifyClient(aClient)}
        />
      </div>
    )
  }
}
