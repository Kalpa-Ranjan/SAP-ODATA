



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HWFRK7H%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T060821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHCUgiy8yU0Mjwj2VXsNRYQ4BnWUrn1y3KblpElfXSyRAiEA6zx20VfTdKG7mXMpui0XRlkjKa5kG7rT9x9xrC6MVPwq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDB%2FpWUrW3Yy66WAdyircA8R7VhHo3a%2BcxQQPCa7JKRLbef1ik52Q%2F%2F34M5foAfYpGoWKWvYKBl7Df4shSWmOVPp8PYW8Xsrg%2Bm3SKVIagggkBbVUAOsa3RXvIeygP42axsAR%2BKbRXzKur%2FpfHwF%2Fu%2FeHZ73udjv2Qewm7uOUDRcuN6i5FRtdBDUkToROccuGPlYc9OOuq61TIxbeNQ3W6f4D3Tdi84U9GlTvjuGMWNa8%2FCRnzFqjjdswUVzjRr3OiTXCjRpTUtClZRXTyWX%2FKmreWsiYqauXkHTJrYXHSfZxttGnll5TLDnc%2FbdmYu4GLEwBetEOtSN5aS27IR97NHi4Dj89hf%2BztWP%2BBQPP5%2F9E%2Fxyi4WPPVGkofos8h21W3%2BIyfNmIMSwaSvQ0pFqfnjoVUguQyHs5iYkegobMJ74aOCV2XFdT%2ByI%2F%2BD%2BfXb9n5kyz8rapyqRXrTR84vx2is%2FKgwcHT0OyqhZZcTCvt52muRCQxP2XejwZ2et6tlkv1XSL9lDKVvaVmju0C4NL%2FG1rxWFKnMWSn6KmCp5etK3dwE305BBcCP1wrXvOmv5Je%2F%2FjrQGgqjymN5Z9Skd3%2FYhQ1xgBSiMt7IFjnOkfmw9rgvt%2FnFiTKAfMxRkrO0cM%2FTql7NIGXUpqXVVXML2M%2BtcGOqUBJ%2Bnlf6uJ9gXmRzXfpT436VBdjZP9t6fEG6mWtshlD9ZYnD0pntce9v%2FJnPu%2BiFnNu5eTxBTETvlXOQaZDjRznZe18WK%2FrvJjgjRmKpcpIJ3XARr1zMtFq5x9SRkecbnF2Z1iPKI%2BIWM9yfG6YIrXBP1isbhcLIY5UR0b02ZOPaAGsRTsaoshp%2BH4zORpHRv9AQ%2BgpJwYq2dbowfZDPC4pQJdtWRk&X-Amz-Signature=46690aa9e822f76d53f9d010cb0d2864e1167e000474c5e7c9b7a8457e804336&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HWFRK7H%2F20261119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261119T060821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEUaCXVzLXdlc3QtMiJHMEUCIHCUgiy8yU0Mjwj2VXsNRYQ4BnWUrn1y3KblpElfXSyRAiEA6zx20VfTdKG7mXMpui0XRlkjKa5kG7rT9x9xrC6MVPwq%2FwMIDRAAGgw2Mzc0MjMxODM4MDUiDB%2FpWUrW3Yy66WAdyircA8R7VhHo3a%2BcxQQPCa7JKRLbef1ik52Q%2F%2F34M5foAfYpGoWKWvYKBl7Df4shSWmOVPp8PYW8Xsrg%2Bm3SKVIagggkBbVUAOsa3RXvIeygP42axsAR%2BKbRXzKur%2FpfHwF%2Fu%2FeHZ73udjv2Qewm7uOUDRcuN6i5FRtdBDUkToROccuGPlYc9OOuq61TIxbeNQ3W6f4D3Tdi84U9GlTvjuGMWNa8%2FCRnzFqjjdswUVzjRr3OiTXCjRpTUtClZRXTyWX%2FKmreWsiYqauXkHTJrYXHSfZxttGnll5TLDnc%2FbdmYu4GLEwBetEOtSN5aS27IR97NHi4Dj89hf%2BztWP%2BBQPP5%2F9E%2Fxyi4WPPVGkofos8h21W3%2BIyfNmIMSwaSvQ0pFqfnjoVUguQyHs5iYkegobMJ74aOCV2XFdT%2ByI%2F%2BD%2BfXb9n5kyz8rapyqRXrTR84vx2is%2FKgwcHT0OyqhZZcTCvt52muRCQxP2XejwZ2et6tlkv1XSL9lDKVvaVmju0C4NL%2FG1rxWFKnMWSn6KmCp5etK3dwE305BBcCP1wrXvOmv5Je%2F%2FjrQGgqjymN5Z9Skd3%2FYhQ1xgBSiMt7IFjnOkfmw9rgvt%2FnFiTKAfMxRkrO0cM%2FTql7NIGXUpqXVVXML2M%2BtcGOqUBJ%2Bnlf6uJ9gXmRzXfpT436VBdjZP9t6fEG6mWtshlD9ZYnD0pntce9v%2FJnPu%2BiFnNu5eTxBTETvlXOQaZDjRznZe18WK%2FrvJjgjRmKpcpIJ3XARr1zMtFq5x9SRkecbnF2Z1iPKI%2BIWM9yfG6YIrXBP1isbhcLIY5UR0b02ZOPaAGsRTsaoshp%2BH4zORpHRv9AQ%2BgpJwYq2dbowfZDPC4pQJdtWRk&X-Amz-Signature=3cc3e5715a18c65bd739ab67cba29e670a2eeae2e160bf59050093c5d021b8d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







