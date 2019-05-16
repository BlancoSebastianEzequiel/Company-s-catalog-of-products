import React from 'react'
import { Button, Col, ControlLabel, Form, FormControl, FormGroup, Grid, Row, HelpBlock } from 'react-bootstrap'
import PropTypes from 'prop-types'

export default class RegisterForm extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      first_name: '',
      last_name: '',
      user_name: '',
      email: '',
      password: '',
      dni: '',
      type: 'client',
      passConfirmation: ''
    }
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

  showField (field, name, type) {
    return (
      <FormGroup controlId={name}>
        <Col componentClass={ControlLabel} sm={2}>
          {name}
        </Col>
        <Col sm={10}>
          <FormControl
            type={type}
            placeholder={name}
            onChange={this.handleChange(field)}
          />
          <HelpBlock>
            <p className="text-danger">{this.props.errors.message}</p>
          </HelpBlock>
        </Col>
      </FormGroup>
    )
  }

  render () {
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <h1 style={{ textAlign: 'center' }} > Register </h1>
          </Col>
        </Row>

        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <Form horizontal>
              {this.showField('first_name', 'first name', 'text')}
              {this.showField('last_name', 'last name', 'text')}
              {this.showField('user_name', 'user name', 'text')}
              {this.showField('email', 'email', 'email')}
              {this.showField('password', 'password', 'password')}
              {this.showField('dni', 'DNI', 'text')}
              {this.showField('passConfirmation', 'Confirm Password', 'password')}
              <FormGroup>
                <Col smOffset={2} sm={10}>
                  <Button type="submit" onClick={ this.submit }>
                    Submit
                  </Button>
                </Col>
              </FormGroup>
            </Form>
          </Col>
        </Row>
      </Grid>
    )
  }
}

RegisterForm.propTypes = {
  onClick: PropTypes.func,
  errors: PropTypes.string
}
