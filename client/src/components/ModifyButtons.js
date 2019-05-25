import React from 'react'
import { Col, Button } from 'react-bootstrap'
import PropTypes from 'prop-types'
import Auth from '../service/Auth'

export default class ListForm extends React.Component {

  render () {
    if (!Auth.isAdmin()) {
      return (null)
    }
    return (
      <Col smOffset={4} sm={10}>
        <Button type="button" onClick={ () => this.props.deleteObject(this.props.anObject) }>
          Delete
        </Button>
        <Button type="button" onClick={ () => this.props.modifyObject(this.props.anObject) }>
          Modify
        </Button>
      </Col>
    )
  }
}

ListForm.propTypes = {
  anObject: PropTypes.object,
  deleteObject: PropTypes.func,
  modifyObject: PropTypes.func,
  permissionToModify: PropTypes.bool
}
