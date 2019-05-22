import React from 'react'
import { Col, Form, Grid, Row, Button } from 'react-bootstrap'
import PropTypes from 'prop-types'

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
            <Col smOffset={4} sm={10}>
              <Button type="button" onClick={ () => this.submit(anObject) } style={{ margin: '1em' }}>
                Delete
              </Button>
              <Button type="button" onClick={ () => this.props.modifyObject(anObject) }>
                Modify
              </Button>
            </Col>
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
