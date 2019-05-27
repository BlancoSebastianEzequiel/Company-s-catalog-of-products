import React from 'react'
import { Button, Col, ControlLabel, FormControl, FormGroup, Grid, Row, HelpBlock } from 'react-bootstrap'
import PropTypes from 'prop-types'

export default class RegisterForm extends React.Component {
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
        <ControlLabel>{title}</ControlLabel>
        <FormControl
          type={type}
          placeholder={placeholder}
          onChange={this.handleChange(fieldName)}
        />
        <HelpBlock>
          <p className="text-danger">{this.props.errors.message}</p>
        </HelpBlock>
      </FormGroup>
    )
  }

  render () {
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <h1 style={{ textAlign: 'center' }} > {this.props.title} </h1>
          </Col>
        </Row>

        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <div>
              { this.props.fields.map((aField, idx) =>
                <div className="panel panel-default" key={idx}>
                  {this.showField(aField)}
                </div>
              )}
            </div>
            <FormGroup>
              <Button type="submit" onClick={ this.submit }>
                  Submit
              </Button>
            </FormGroup>
          </Col>
        </Row>
      </Grid>
    )
  }
}

RegisterForm.propTypes = {
  onClick: PropTypes.func,
  errors: PropTypes.object,
  fields: PropTypes.array,
  fieldsState: PropTypes.object,
  title: PropTypes.string
}
