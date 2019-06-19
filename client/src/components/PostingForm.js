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

  getBase64 = (file) => {
    return new Promise((resolve,reject) => {
       const reader = new FileReader();
       reader.onload = () => resolve(reader.result);
       reader.onerror = error => reject(error);
       reader.readAsDataURL(file);
    })
  }

  fileSelectedHandler = name => event => {
    const file = event.target.files[0];
    this.getBase64(file).then(base64 => {
      let filesList = this.state[name]
      filesList.push(base64)
      this.setState({
        [name]: filesList
      })
    })
  }

  submit = (event) => {
    event.preventDefault()
    this.props.onClick(this.state)
  }

  showField (fieldData) {
    const { placeholder, fieldName, type, title } = fieldData
    let handler
    if (type === 'file') {
      handler = this.fileSelectedHandler(fieldName)
    } else {
      handler = this.handleChange(fieldName)
    }
    return (
      <FormGroup controlId={fieldName}>
        <ControlLabel>{title}</ControlLabel>
        <FormControl
          type={type}
          placeholder={placeholder}
          accept="application/gzip, .png"
          multiple="true"
          onChange={handler}
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
