import React from 'react'
import { Col, Row, HelpBlock, FormControl, FormGroup, Button, ControlLabel } from 'react-bootstrap'
import PropTypes from 'prop-types'

export default class FilterNavForm extends React.Component {
  constructor (props) {
    super(props)
    this.state = this.props.fieldsState
  }

  handleChange = name => event => {
    this.setState({
      [name]: event.target.value
    })
  }

  submit = (event) => {
    event.preventDefault()
    this.props.onClick(this.state)
  }

  showField (fieldData) {
    const { placeholder, fieldName, type, title } = fieldData
    return (
      <FormGroup controlId={fieldName}>
        <Col componentClass={ControlLabel} sm={2}>
          {title}
        </Col>
        <Col>
          <FormControl
            type={type}
            placeholder={placeholder}
            onChange={this.handleChange(fieldName)}
          />
          <HelpBlock>
            <p className="text-danger">{this.props.errors.message}</p>
          </HelpBlock>
        </Col>
      </FormGroup>
    )
  }

  render () {
    if (!this.props.showSearchNavBar) return (null)
    return (
      <Col sm={4}>
        <Row className="show-grid">
          <h1 style={{ textAlign: 'center' }} > {this.props.title} </h1>
        </Row>
        <Row className="show-grid">
          <div>
            { this.props.fields.map((aField, idx) =>
              <div className="panel panel-default" key={idx}>
                {this.showField(aField)}
              </div>
            )}
          </div>
          <FormGroup>
            <Col smOffset={2} sm={10}>
              <Button type="submit" onClick={ this.submit }>
                Submit
              </Button>
            </Col>
          </FormGroup>
        </Row>
      </Col>
    )
  }
}

FilterNavForm.propTypes = {
  onClick: PropTypes.func,
  errors: PropTypes.object,
  fields: PropTypes.array,
  fieldsState: PropTypes.object,
  title: PropTypes.string,
  showSearchNavBar: PropTypes.bool
}
