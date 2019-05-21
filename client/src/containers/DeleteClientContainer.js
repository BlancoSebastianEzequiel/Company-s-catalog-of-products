import React from 'react'
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
      }]
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
    const { errors, clients } = this.state
    return (
      <div>
        <ToastContainer></ToastContainer>
        <ListForm
          errors={errors}
          ObjectsList={clients}
          getList={() => this.getClients()}
          deleteObject={(anObject => this.deleteClient(anObject))}
        />
      </div>
    )
  }
}
