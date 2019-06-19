import React from 'react'
import { Col, Form, Grid, Row, FormGroup, Button } from 'react-bootstrap'
import Markdown from 'react-markdown'
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

  shouldShow (list) {
    if (list.length === 0) return false
    if (list[0]._id === '') return false
    return true
  }

  showList () {
    if (!this.shouldShow(this.props.ObjectsList)) {
      return (null)
    }
    return (
      <div>
        { this.props.ObjectsList.map((anObject, idx) =>
          <div className="panel panel-default" key={idx}>
            <Markdown className="text-display" id="text-display" >
              {anObject.data}
            </Markdown>
            <img src={anObject.file[0]} alt="no images"/>
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
          showSearchNavBar={this.props.showSearchNavBar}
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
  title: PropTypes.string,
  dataName: PropTypes.string,
  showSearchNavBar: PropTypes.bool
}
