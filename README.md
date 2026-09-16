



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVTZNVHS%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T121146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIBcGf%2FXONO02NsjfsavmJ4I46la4I0D0PP7Htm%2F8FcH7AiEAogqg1%2BM546g%2FwIhoke7u9u6Q1bvfnqzDLuWsAS69fugq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDItAREG5YxH3j8z0sircA%2B9lQ0YJeoVOJaaxmXNVR6TM%2F1pkoWkpR4ghzx2q6szTdEn%2FdqWZWpg2jYdhPAPICa%2F6iE54qxjIb7V8tVGAKFUYigsgYjqy15YNe3%2B5pZIwn%2B0PRtioyrTGD6voA5M7MAEkeBb2MvGrI8m80TDi2vA5rww93Nb%2Bzkya%2B9%2BeMcUAKIC8H%2F096IoqYZ51TK1XIzq0AX18O%2F3IL0QoxqaJ0q7axcgf5v%2F5VX2DxyE7NCJas2VbieOI6L9clJL76vGAwahZFqNOXmsIQ8kr52TN2Io8IOoa%2FcnqPTBjigc2nBgr04F1dUR0UB%2BkEDOY7kMrhcDZYPpSDBmd%2FFjjjAY3RuW75vLXzrVekWuXxUFOdA38eZpS5sKdysx5F9VOL9WQMeQaHOB79SAvq30GPCmao6AvUY4CXmaUKRUXv74tKOOEwgN%2FPoDEr3t8byn3B9V7gG6uM3UTE8ZYzK6hd1JxQU4nL6I3jYu1JlhrvzAOsloU%2FVlnB6JoSAQ3fVTbNu60m1sm9%2FBWKTDeSoKY1G94PwxBjGgdokviuJ%2BNdgW9RNRcrifQk6U8qJBkIDieSoUJSY0elRxsYkwdE%2BTrDFjNOd%2BQB6iT8rqEl4GQR5E1juTMbixyEQbgs9RA4D9%2FMPiJqtUGOqUBcIWuwY8hHMpBypmL5GnUGNgNLaUDccHukHxvHxvJu5vkpuDuqigETdZwSIvX8H74so0c4UTFd9rycdBO9PHjEbGZ0pseSTIbzP8eoQJ%2FxLvJBrPNrQ%2BayA7hlNskjPumcGRyukp4db46OWmeMl6PXcHe%2BmFTzkY32vUUp8jIoTaKA2KRK5lPrqV6uojCT1ua45KoVENOZZ7UCQU6iwMzC1wyutEB&X-Amz-Signature=e1ba66663cca528916d3dcf988d06f7d43ffbadc25ca259ac27268679aa9cf23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVTZNVHS%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T121146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIBcGf%2FXONO02NsjfsavmJ4I46la4I0D0PP7Htm%2F8FcH7AiEAogqg1%2BM546g%2FwIhoke7u9u6Q1bvfnqzDLuWsAS69fugq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDItAREG5YxH3j8z0sircA%2B9lQ0YJeoVOJaaxmXNVR6TM%2F1pkoWkpR4ghzx2q6szTdEn%2FdqWZWpg2jYdhPAPICa%2F6iE54qxjIb7V8tVGAKFUYigsgYjqy15YNe3%2B5pZIwn%2B0PRtioyrTGD6voA5M7MAEkeBb2MvGrI8m80TDi2vA5rww93Nb%2Bzkya%2B9%2BeMcUAKIC8H%2F096IoqYZ51TK1XIzq0AX18O%2F3IL0QoxqaJ0q7axcgf5v%2F5VX2DxyE7NCJas2VbieOI6L9clJL76vGAwahZFqNOXmsIQ8kr52TN2Io8IOoa%2FcnqPTBjigc2nBgr04F1dUR0UB%2BkEDOY7kMrhcDZYPpSDBmd%2FFjjjAY3RuW75vLXzrVekWuXxUFOdA38eZpS5sKdysx5F9VOL9WQMeQaHOB79SAvq30GPCmao6AvUY4CXmaUKRUXv74tKOOEwgN%2FPoDEr3t8byn3B9V7gG6uM3UTE8ZYzK6hd1JxQU4nL6I3jYu1JlhrvzAOsloU%2FVlnB6JoSAQ3fVTbNu60m1sm9%2FBWKTDeSoKY1G94PwxBjGgdokviuJ%2BNdgW9RNRcrifQk6U8qJBkIDieSoUJSY0elRxsYkwdE%2BTrDFjNOd%2BQB6iT8rqEl4GQR5E1juTMbixyEQbgs9RA4D9%2FMPiJqtUGOqUBcIWuwY8hHMpBypmL5GnUGNgNLaUDccHukHxvHxvJu5vkpuDuqigETdZwSIvX8H74so0c4UTFd9rycdBO9PHjEbGZ0pseSTIbzP8eoQJ%2FxLvJBrPNrQ%2BayA7hlNskjPumcGRyukp4db46OWmeMl6PXcHe%2BmFTzkY32vUUp8jIoTaKA2KRK5lPrqV6uojCT1ua45KoVENOZZ7UCQU6iwMzC1wyutEB&X-Amz-Signature=6d2e4372fc6e47f2216949462df4a2abce972d023422a156ab4080c08c61dfd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







