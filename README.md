



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQNMGDAX%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T180923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfOk%2FdKFAApRZhGvpwdub0f5AhTyLuxRZythPOln6sWAIgRsQa86oD%2BIHTi%2FS2tDjEGH7%2BDPI0uDN9j8Bkcu%2Bevd0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDfTqHyj1XMy%2FAWExyrcA39gqMFPMSLyBE3S%2BWVfOJALph0aTR64qsLMLQReEs0EH2YxYGEVJXRd7ZuDfB3uEi%2BrgS0qHgQHDD%2BM2gL4lXAJ00g4vFmxBPq3veCKWJCMMtG7bey2rxxCW7IZRAuew3sA7cag8V3thuhp9NRM74nelMO66QLCw9b%2Fq%2Fg04dU%2FZUNeJQodT38CNIc6vBX97KffOiPvpQdcvp%2BJ4td1d8MYtOA0xqBX%2FgRdCyDtDt7ttM01%2BaN9%2F2rktP2KV5a1siFSAgjDltPmWHkhXcCU8b18iJ6sZ%2BdwfBj%2BT%2BYntKKJpg5HSIhFzyRCf%2B5TqZW%2F0XYbdqdTuu5F9zMW71bJgS2326RpNdmSilNvf7BSb7qzdR2y7cNwcSurlQvHnNtq7YBPhtiK4sMfWxaqTt9wXg5x2sR9D%2FyIr%2FqBaWYp6PFdhqbxpVdJHTGXcOCAX5tV6bJr377nFJRT88tC9Ble5tuuPVEFAHk66XG%2Bc6WE21nHtPfm%2F674xp%2FN3dx3kQKoOfH6Ns5%2F46KQiiZ3kYUPiQpbPf4xFIjk97%2BUP2HJLY6S9GnDy%2B5GzUWUI6L3aBQW4lbmXpNvhlnpiIzoiNXvuDpnEZzqlbIrALhcrhteHDYu5yEzsCP6S3X%2BG3LfMJaE6dYGOqUBrGaUk%2BnUdtwNig0uIHJ1eHXGMts9qorgil8bU1UkSyG21%2BWZr7l6jC1Nd9yubT6oaxbORi5n9QvnI83XmRxPjf9Pk7aS8YCMM7ktI83yR8unw5D70jTirY6lbrF2pCpCkDcOQJb%2FhQJh3HiBZDhEVJ76k%2Bi%2Fh2E%2BstQKH0iBMKuiAxsMg4XJqQROK3UtDyBQ7mI2OZKB3nfBEqXmZnrfRXepsi8g&X-Amz-Signature=e710e98606fcfc3e4918cf70403cb25cf646ff8fee6b313e46f1342c7350e5ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QQNMGDAX%2F20261022%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T180923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCfOk%2FdKFAApRZhGvpwdub0f5AhTyLuxRZythPOln6sWAIgRsQa86oD%2BIHTi%2FS2tDjEGH7%2BDPI0uDN9j8Bkcu%2Bevd0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDfTqHyj1XMy%2FAWExyrcA39gqMFPMSLyBE3S%2BWVfOJALph0aTR64qsLMLQReEs0EH2YxYGEVJXRd7ZuDfB3uEi%2BrgS0qHgQHDD%2BM2gL4lXAJ00g4vFmxBPq3veCKWJCMMtG7bey2rxxCW7IZRAuew3sA7cag8V3thuhp9NRM74nelMO66QLCw9b%2Fq%2Fg04dU%2FZUNeJQodT38CNIc6vBX97KffOiPvpQdcvp%2BJ4td1d8MYtOA0xqBX%2FgRdCyDtDt7ttM01%2BaN9%2F2rktP2KV5a1siFSAgjDltPmWHkhXcCU8b18iJ6sZ%2BdwfBj%2BT%2BYntKKJpg5HSIhFzyRCf%2B5TqZW%2F0XYbdqdTuu5F9zMW71bJgS2326RpNdmSilNvf7BSb7qzdR2y7cNwcSurlQvHnNtq7YBPhtiK4sMfWxaqTt9wXg5x2sR9D%2FyIr%2FqBaWYp6PFdhqbxpVdJHTGXcOCAX5tV6bJr377nFJRT88tC9Ble5tuuPVEFAHk66XG%2Bc6WE21nHtPfm%2F674xp%2FN3dx3kQKoOfH6Ns5%2F46KQiiZ3kYUPiQpbPf4xFIjk97%2BUP2HJLY6S9GnDy%2B5GzUWUI6L3aBQW4lbmXpNvhlnpiIzoiNXvuDpnEZzqlbIrALhcrhteHDYu5yEzsCP6S3X%2BG3LfMJaE6dYGOqUBrGaUk%2BnUdtwNig0uIHJ1eHXGMts9qorgil8bU1UkSyG21%2BWZr7l6jC1Nd9yubT6oaxbORi5n9QvnI83XmRxPjf9Pk7aS8YCMM7ktI83yR8unw5D70jTirY6lbrF2pCpCkDcOQJb%2FhQJh3HiBZDhEVJ76k%2Bi%2Fh2E%2BstQKH0iBMKuiAxsMg4XJqQROK3UtDyBQ7mI2OZKB3nfBEqXmZnrfRXepsi8g&X-Amz-Signature=2da52cecdc736b2686f5aca94fce2a7b3ea7b0491daad33a7e54d59bbc2ccf46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







