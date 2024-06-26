# **SAVEX**

## Overview

SaveX is a Python library crafted to bolster the security of file uploads within web applications. With an emphasis on mitigating prevalent vulnerabilities associated with file handling, SaveX furnishes sturdy sanitization and validation capabilities to ensure that uploaded files are safe for utilization within your application.

:star: If you find savex useful, please consider giving us a star on GitHub! Your support helps us continue to innovate and deliver exciting features.

![GitHub contributors](https://img.shields.io/github/contributors/aliftech/savex)
![GitHub Repo stars](https://img.shields.io/github/stars/aliftech/savex)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/aliftech/savex/master)
![GitHub release (with filter)](https://img.shields.io/github/v/release/aliftech/savex)
![GitHub License](https://img.shields.io/github/license/aliftech/savex)

## Key Features

1. **File Name Sanitization:** Savex provides functions to sanitize file names by eliminating disallowed characters, consecutive dots or spaces, and thwarting path traversal attempts. This thwarts malicious users from exploiting file upload functionalities to compromise the server.

2. **Content Validation:** The library encompasses mechanisms to execute basic content checks on uploaded files. It scrutinizes file contents for suspicious patterns, such as PHP or JavaScript code injections, and identifies potential backdoor attempts within image files.

3. **File Type Verification:** Savex validates the file types of uploads to ensure compliance with allowed formats. By scrutinizing file extensions and content headers, it prevents the execution of arbitrary code masquerading as benign file uploads.

4. **Customizable Security Policies:** Developers can tailor security policies to suit their application's requirements. SaveX facilitates fine-tuning of permitted file extensions, content patterns, and backdoor detection mechanisms, offering flexibility while upholding security.

## Benefits

- **Enhanced Security:** By integrating SaveX into your file upload workflow, you can significantly diminish the risk of security breaches and safeguard your application from malevolent file uploads.

- **Ease of Integration:** With its intuitive API and straightforward usage, SaveX seamlessly integrates into existing Python-based web applications, necessitating minimal setup and configuration.

- **Comprehensive Protection:** SaveX addresses diverse security concerns related to file uploads, furnishing a comprehensive solution for fortifying your application's file handling functionalities.

## Target Audiences

Savex caters to developers and organizations constructing web applications that involve user-generated content and file uploads. It serves individuals and teams striving to fortify their application's defenses against common security threats linked with file handling vulnerabilities.

## Future Development

In forthcoming iterations, Savex aims to integrate advanced security features, including real-time threat detection, enhanced file analysis techniques, and amalgamation with security frameworks for comprehensive protection against evolving cyber threats. Furthermore, the project will concentrate on augmenting usability and performance to deliver an even more robust and user-friendly solution.

## Instalation

```bash
pip install savex
```

## Quick Start

```python
def main():
    # Create a mock file object
    class MockFile:
        def __init__(self, name):
            self.name = name

    # Test valid file name
    valid_file = MockFile("foto.jpg.php")
    print(file_filter(valid_file))


if __name__ == "__main__":
    main()

```

## Contributing

Kindly read our [Contributing Guide](CONTRIBUTING.md) to familiarize yourself with ToolJet's development process, how to suggest bug fixes and improvements, and the steps for building and testing your changes. <br>

## Contributors

<a href="https://github.com/aliftech/savex/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=aliftech/savex" />
</a>

## License

Savex © 2024, Released under the MIT License.
