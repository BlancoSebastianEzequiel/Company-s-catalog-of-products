import React from 'react'
import { ToastContainer, toast } from 'react-toastify'
import ListForm from '../components/ListForm'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class ActivePrincipleListContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      errors: {},
      refresh: false,
      activePrinciples: [{
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

  getActivePrinciples = () => {
    if (this.state.refresh) return
    let ActivePrincipleVector = []
    Http.get('/active_principle/')
      .then(response => {
        if (response.status === httpStatus.OK) {
          const length = response.content.data.length
          for (let i = 0; i < length; i++) {
            const anActivePrinciple = response.content.data[i]
            const _id = response.content.data[i]._id
            ActivePrincipleVector.push(
              {
                'data': 'CODE: ' + anActivePrinciple['code'] + ' -- NAME: ' + anActivePrinciple['name'],
                '_id': _id
              })
          }
          this.handleChange('activePrinciples', ActivePrincipleVector)
          this.handleChange('refresh', false)
        } else {
          toast('ERROR: ' + response.content.data)
        }
      })
      .catch(err => {
        toast('ERROR: ' + err)
      })
  }

  deleteActivePrinciple = (anActivePrinciple) => {
    Http.delete('/active_principle/', anActivePrinciple._id)
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
    const { errors, activePrinciples } = this.state
    return (
      <div>
        <ToastContainer></ToastContainer>
        <ListForm
          errors={errors}
          ObjectsList={activePrinciples}
          getList={() => this.getActivePrinciples()}
          deleteObject={(anObject => this.deleteActivePrinciple(anObject))}
        />
      </div>
    )
  }
}
