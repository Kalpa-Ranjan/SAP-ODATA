



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWNGIPMH%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T064119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBh1LvEPbrAqvax45NwH5dKxoZG%2B1BqV%2BUrkLAtAi6p5AiEA5QaEJXwhQ4vYtpMDRnb6k7F0j5zf1i2DfFJ54dBG0ZYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDET86vG0lZrmksPCAircA3XQc1CDThidY7VdPwrDw4z1ecIhquK5cw1cHz0UTEI7h%2FR2kFCUhO9RQVYHkft5ylIF9554QKf9UzSZyjkyIF9HNNW9wOAAps8FG%2FMlHDaH9FpFeywM7CmtT6MXNRNDBXMIZcW%2FkWFkl04gls0iMMQCHLXFy2Ra860bJOZAND24oGg2qZCrf5Tnf5rpbEXJsNWZHF0JnXHHQ05G1eUk0OwthEW75q%2FK3czh9%2F3hq%2BbG%2F1Fr4V3I%2BqKUXq8Xuvoh8X56CtALuBE03QCyPdPXOLNlqsTLtd3mrRYNOWhWQVlsdammaVxrT4gjZhMqfUApxqcPFwng8K89WNAI6DzDMbHYFVEVuqJGOdDdEkJ9Vm8A1zHJT%2BS5wBgAj0FhfTi3dSsusQJXfU%2BElx0G0elIJ39p7x4LSGZ5jm%2BN54YQal1%2F40GQODakrSeTSW%2Bg%2Fll0h53vVe7SiZSFoxSgp5rJwFTFvNbnlJACWK0kuiqt0xKrO%2FW8LkRvtzTWd%2B77QsS9yi8ljWX4d6DsvmSqvQvrTIpuwvJZKXgGZjmAzXXPKWhduL1aL48mebYOr%2FSoLIKfg3ba3oFQPBuJw7KigrB88KZXS%2BGKWaA8XHo6FTSl1wxbu32y12gBX%2F1fDgdDMPfs2tMGOqUBuT4WKKMsuJiARXFxgisnVpaAI2ckArK%2BR1PQKf6FBJ1PRdtMMKrpxQwYm%2BHCH5OTd%2BslSnuqV3aw0km494gwWnjxiUnpmVRVXN5AaGHN4iBBxzcQbWUOaf%2FWu8DnEKN6hR9cgACn5970aBGpY6wrFj%2Fk2WkhgnlXnXhgUYU1UJUB%2Br%2BBUEu85tapLdcfptq%2Faky9wBST%2FPhfkj8aiBumuv5d0ncC&X-Amz-Signature=8b128f29bcf9c19447397a68b061739699e2df5fc01adc8583822a2a0563f7cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWNGIPMH%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T064119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBh1LvEPbrAqvax45NwH5dKxoZG%2B1BqV%2BUrkLAtAi6p5AiEA5QaEJXwhQ4vYtpMDRnb6k7F0j5zf1i2DfFJ54dBG0ZYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDET86vG0lZrmksPCAircA3XQc1CDThidY7VdPwrDw4z1ecIhquK5cw1cHz0UTEI7h%2FR2kFCUhO9RQVYHkft5ylIF9554QKf9UzSZyjkyIF9HNNW9wOAAps8FG%2FMlHDaH9FpFeywM7CmtT6MXNRNDBXMIZcW%2FkWFkl04gls0iMMQCHLXFy2Ra860bJOZAND24oGg2qZCrf5Tnf5rpbEXJsNWZHF0JnXHHQ05G1eUk0OwthEW75q%2FK3czh9%2F3hq%2BbG%2F1Fr4V3I%2BqKUXq8Xuvoh8X56CtALuBE03QCyPdPXOLNlqsTLtd3mrRYNOWhWQVlsdammaVxrT4gjZhMqfUApxqcPFwng8K89WNAI6DzDMbHYFVEVuqJGOdDdEkJ9Vm8A1zHJT%2BS5wBgAj0FhfTi3dSsusQJXfU%2BElx0G0elIJ39p7x4LSGZ5jm%2BN54YQal1%2F40GQODakrSeTSW%2Bg%2Fll0h53vVe7SiZSFoxSgp5rJwFTFvNbnlJACWK0kuiqt0xKrO%2FW8LkRvtzTWd%2B77QsS9yi8ljWX4d6DsvmSqvQvrTIpuwvJZKXgGZjmAzXXPKWhduL1aL48mebYOr%2FSoLIKfg3ba3oFQPBuJw7KigrB88KZXS%2BGKWaA8XHo6FTSl1wxbu32y12gBX%2F1fDgdDMPfs2tMGOqUBuT4WKKMsuJiARXFxgisnVpaAI2ckArK%2BR1PQKf6FBJ1PRdtMMKrpxQwYm%2BHCH5OTd%2BslSnuqV3aw0km494gwWnjxiUnpmVRVXN5AaGHN4iBBxzcQbWUOaf%2FWu8DnEKN6hR9cgACn5970aBGpY6wrFj%2Fk2WkhgnlXnXhgUYU1UJUB%2Br%2BBUEu85tapLdcfptq%2Faky9wBST%2FPhfkj8aiBumuv5d0ncC&X-Amz-Signature=3b3df8dbea1534ec2e1b2cd7e5383dde33238dd2f5d08e7467a158154168bd12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







