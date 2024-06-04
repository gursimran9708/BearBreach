# BearBreach 🐻🔒

![](path_to_your_logo_image.png)![BEAR BREACH FULL LOGO](https://github.com/gursimran9708/BearBreach/assets/82988478/5db213e4-1b28-4972-bd92-292954fde91f)


BearBreach is a comprehensive tool designed for cybersecurity professionals. It allows users to leverage public APIs of popular threat intelligence platforms like Virustotal, Aienvault, Polyswarm, OPSWAT and many more. This tool can be used by SOC analysts, Threat Hunters and Incident responders to query an IOC on multiple threat intelligence platforms at once without the hassle of going to different platforms using web and log in into them individually. Here we just have to register on all of these platorms for once and get their public API keys and that's all authentication you need to use these platforms to your benefit.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features ✨

- **Command Line Based**: Easy access through your shell/terminal.
- **Free Threat Intelligence**: Utilize public APIs of popular threat platforms to improve your detection.
- **Comprehensive Threat Analysis**: Gain insights into the nature and impact of detected threats.
- **Minimal Setup**: Follow easy steps and use in your environment.
- **Multiple Data Sources**: Don't rely on a single source for threat intelligence data, leverage multiple sources using BearBreach.

## Installation 🛠️

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/gursimran9708/BearBreach.git
    cd bearbreach
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
    
3. Setting up the API Keys :

    ```bash
    nano .env 
    ```
    You only need to visit following threat intelligence platfroms, create account and retrieve your API keys:
   
    https://www.virustotal.com/gui/         
    https://www.criminalip.io/              
    https://malshare.com/                                        
    https://www.abuseipdb.com/                                       
    https://hybrid-analysis.com/docs/api/v2                                       
    https://bazaar.abuse.ch/                                       
    https://metadefender.opswat.com/                                       
    https://www.greynoise.io/                                        
    https://otx.alienvault.com/api                                        
    https://polyswarm.network/
                                    
## Usage 🚀

1. Configure the application (see [Configuration](#configuration) section).
2. Run the application (make sure you are inside the folder where "grizzy.py" file is present):

    ```bash
    python grizzy.py
    ```

3. TADAAAA !.

## Configuration ⚙️

Here we will populate our API key variables:

1. Open the ".env" in a text editor and fill all the fields with their respective keys and hit save.
   Following are the fields that you'll encounter -

        VT_API_KEY=""
        CRIMINALIP_API_KEY=""
        MALSHARE_API_KEY=""
        ABUSEIPDB_API_KEY=""
        FALCON_API_KEY=""
        MALWAREBAZAAR_API_KEY=""
        OPSWAT_API_KEY=""
        GREYNOISE_API_KEY=""
        OTX_API_KEY=""
        POLYSWARM_API_KEY=""

## Contact 📞
Mail: gursimransinghwadhawan@gmail.com

Linkedin: https://in.linkedin.com/in/gursimransw

Medium: https://medium.com/@gursimransw
