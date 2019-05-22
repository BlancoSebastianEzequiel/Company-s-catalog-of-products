import React from 'react'
import { Redirect } from 'react-router-dom'
import { ToastContainer, toast } from 'react-toastify'
import ListForm from '../components/ListForm'
import Http from '../service/Http'
import httpStatus from 'http-status-codes'

export default class ActivePrincipleListContainer extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      errors: {},
      refresh: true,
      activePrinciples: [{
        'data': '',
        '_id': ''
      }],
      redirectTo: false,
      urlToRedirect: '/modify-active-principle',
      dataToRedirect: {}
    }
  }

  handleChange = (name, value) => {
    this.setState({
      [name]: value
    })
  }

  getActivePrinciples = () => {
    if (!this.state.refresh) return
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

  modifyActivePrinciple = (anActivePrinciple) => {
    this.setState({ redirectTo: true })
    this.setState({ dataToRedirect: anActivePrinciple })
  }

  render () {
    const { errors, activePrinciples, redirectTo, urlToRedirect, dataToRedirect } = this.state
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
          ObjectsList={activePrinciples}
          getList={() => this.getActivePrinciples()}
          deleteObject={(anActivePrinciple => this.deleteActivePrinciple(anActivePrinciple))}
          modifyObject={(anActivePrinciple) => this.modifyActivePrinciple(anActivePrinciple)}
        />
      </div>
    )
  }
}
