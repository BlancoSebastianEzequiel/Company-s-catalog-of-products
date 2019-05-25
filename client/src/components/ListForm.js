import React from 'react'
import { Col, Form, Grid, Row } from 'react-bootstrap'
import PropTypes from 'prop-types'
import ModifyButtons from './ModifyButtons'

export default class ListForm extends React.Component {
  constructor (props) {
    super(props)
    this.state = {}
  }

  handleChange = (name, value) => {
    this.setState({
      [name]: value
    })
  }

  submit = (anObject) => {
    this.props.deleteObject(anObject)
  }

  showList () {
    return (
      <div>
        { this.props.ObjectsList.map((anObject, idx) =>
          <div className="panel panel-default" key={idx}>
            <div className="panel-heading">{anObject.data}</div>
            <ModifyButtons
              anObject={anObject}
              deleteObject={(anObject) => this.props.deleteObject(anObject)}
              modifyObject={(anObject) => this.props.modifyObject(anObject)}
            />
          </div>
        )}
      </div>
    )
  }

  render () {
    this.props.getList()
    return (
      <Grid>
         <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <h1 style={{ textAlign: 'center' }} > {this.props.title} </h1>
          </Col>
        </Row>
        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <Form horizontal>
              { this.showList() }
            </Form>
          </Col>
        </Row>
      </Grid>
    )
  }
}

ListForm.propTypes = {
  getList: PropTypes.func,
  deleteObject: PropTypes.func,
  modifyObject: PropTypes.func,
  errors: PropTypes.object,
  ObjectsList: PropTypes.array
}
