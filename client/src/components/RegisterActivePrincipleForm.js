import React from 'react'
import { Button, Col, ControlLabel, Form, FormControl, FormGroup, Grid, Row, HelpBlock } from 'react-bootstrap'
import PropTypes from 'prop-types'

export default class RegisterActivePrincipleForm extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      code: '',
      name: '',
      description: '',
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
            <h1 style={{ textAlign: 'center' }} > Create active principle </h1>
          </Col>
        </Row>

        <Row className="show-grid">
          <Col xs={12} md={6} mdOffset={3}>
            <Form horizontal>
              {this.showField('code', 'code', 'text')}
              {this.showField('name', 'name', 'text')}
              {this.showField('description', 'description', 'text')}
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

RegisterActivePrincipleForm.propTypes = {
  onClick: PropTypes.func,
  errors: PropTypes.string
}
