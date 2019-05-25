import React from 'react'
import { Col, Form, Grid, Row, FormGroup, Button } from 'react-bootstrap'
import PropTypes from 'prop-types'
import ModifyButtons from './ModifyButtons'
import FilterNavForm from './FilterNavForm'
import data from '../data/data'

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
    return (
      <Grid>
        <FilterNavForm
          errors={this.props.errors}
          onClick={(query) => this.props.getList(query)}
          fields={data[this.props.dataName].searchFields}
          fieldsState={data[this.props.dataName].fieldsStateSearch}
          title={'search'}
          show={this.props.dataName === 'product'}
        />
        <Col sm={8}>
          <Row className="show-grid">
            <h1 style={{ textAlign: 'center' }} > {this.props.title} </h1>
          </Row>
          <Row className="show-grid">
            <Col xs={12} md={6} mdOffset={3}>
              <Form horizontal>
                { this.showList() }
              </Form>
              <FormGroup>
                <Col>
                  <Button type="submit" onClick={ () => this.props.getList(null) }>
                    Update
                  </Button>
                </Col>
              </FormGroup>
            </Col>
          </Row>
        </Col>
      </Grid>
    )
  }
}

ListForm.propTypes = {
  getList: PropTypes.func,
  deleteObject: PropTypes.func,
  modifyObject: PropTypes.func,
  errors: PropTypes.object,
  ObjectsList: PropTypes.array,
  title: PropTypes.object,
  dataName: PropTypes.string
}
