# Social Distancing
Reduce person-to-person contact in order to make spreading the disease less likely.
Spread out the spread of disease in time as much as possible to allow hospitals to 
help every sick patient to minimize deaths, increase survival rate. 

Simulate the situation using SEIR epidemiological model
* S = Sucsceptible
* E = Exposed
* I = Infected
* R = Recovered

Population moves from one stage to the other. 
dS/dt = - rho * beta * S * I
dE/dt = (rho * beta * S * I) - (alpha * I)
dI/dt = (alpha * E) - (gamma * I)
dR/dt = gamma * I

N = S + E + I + R (total population is fixed)

rho is the social distancing effect (Contact rate between people)</br>
Rho = 1 means no social distancing. 0 means everyone is locked down.


## Author
You can get in touch with me on my LinkedIn Profile:-

#### Muhammad Junaid Iqbal
[![LinkedIn Link](https://img.shields.io/badge/LinkedIn-Muhammad%20Junaid%20Iqbal-lightgrey)](https://www.linkedin.com/in/thejunaidiqbal)

You can follow me on my GitHub Profile for more updates on my Open Source Projects:
</br>
[![GitHub Follow](https://img.shields.io/badge/Connect-Muhammad%20Junaid%20Iqbal-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/thejunaidiqbal)

If you liked the repo then kindly support it by giving it a star ⭐⭐⭐⭐⭐!</br>
[![GitHub stars](https://img.shields.io/github/stars/thejunaidiqbal/social-distancing)](https://github.com/thejunaidiqbal/social-distancing/stargazers)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.

## Issues
[![GitHub issues](https://img.shields.io/github/issues/thejunaidiqbal/social-distancing?style=plastic)](https://github.com/thejunaidiqbal/social-distancing/issues)

If you face any issue in my project, you can create a new issue in the "Issues Section" and I will be glad to help you out.


