



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GILGW4P%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T190518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHhHzsbjB7y0h8i%2BHkBMTca0vrRoqIc7JVmLffzfbwXfAiEA7a284LnGhJaj8y2bjaRrGFcbwwDe59ewufTrneA%2FOL4qiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJt4%2BnNnpCsl0614%2ByrcA5G7DmmeTykWn5Ncz5axSj0kVBknGvhfeX7Rr03Lm0t5Ry5ZhikX1TfLhiDn9RLPVABG1JNRfjENSrALIHOj8Nja2P%2BFHm%2Fn4DLNRBD%2BicDLCeB3abnk14d8kwGXn3yNkSNveky2QEIA0cWwl%2BuAa5b8MFuUWbW9T%2BoxRaXY8sqm3VCvYwj0O4XL9wM85XGxO76zcD6xTJoysGA%2FaIAgzmIx1Y3zofYvWTL9eS2mXjUZX76oihknmsFjfw70mqwPdQBpI%2BmdPE6daA4bTuxz2RHgOwfh42ophC8cGwoGIQxgRM71bBpcmgj%2BYm%2FX0RRkxXFXc1z97J5CiQPDDLXcf7KFGCfWm47cH5L2tSAdElVqIiBcTT9az7JD3RgBM7ubwanRcVjsIBTZkXElamjuU9MEFnqUQmIe9jEKNwWIimaBMZKMfzEhyb84BeQB%2F3XmJZClNm%2BNJyDrz4crIujtxNlEg%2B4hGK1gZNxIepeuXVvK07x%2F5kVCvhHabiC5XmWWmfd5Ethov8L2BC3LMAvgMXlu1l32Jh4LN3dyswHdSVg5JEVqa68rqWcXaLlsBmMpcq%2BesixPtt5l1875EFivHmJQ6obZ0zL8r1ZessidxET931maVk9tTaKztXaEMI3g7NAGOqUBWd%2F%2Fl9m2ov7ucrCOwC%2Bjn6aZKUkl7qBtk8G9IaIAFbYZJv9x1T4LH7ugvxzMsU4pkMCc%2FYXk0eDK1J8r48GzTEB%2FlbvCqUD%2FlJe2LD4SVJxYGyN7CWpFeW41wFPkUggXN678qe%2FIP%2FaWoFgPqZa%2FCvKzuSMv1hc0ygjc95FYQuYVjzFtSiT3CyZi7fR25uRjCv%2FhW9jmjxKxNup3VrSVgp%2BbNe0u&X-Amz-Signature=25daf0f92b07309c9bb83e850fbaae974f22a42d975a0694967b5fc1efd73048&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GILGW4P%2F20260530%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260530T190518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHhHzsbjB7y0h8i%2BHkBMTca0vrRoqIc7JVmLffzfbwXfAiEA7a284LnGhJaj8y2bjaRrGFcbwwDe59ewufTrneA%2FOL4qiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJt4%2BnNnpCsl0614%2ByrcA5G7DmmeTykWn5Ncz5axSj0kVBknGvhfeX7Rr03Lm0t5Ry5ZhikX1TfLhiDn9RLPVABG1JNRfjENSrALIHOj8Nja2P%2BFHm%2Fn4DLNRBD%2BicDLCeB3abnk14d8kwGXn3yNkSNveky2QEIA0cWwl%2BuAa5b8MFuUWbW9T%2BoxRaXY8sqm3VCvYwj0O4XL9wM85XGxO76zcD6xTJoysGA%2FaIAgzmIx1Y3zofYvWTL9eS2mXjUZX76oihknmsFjfw70mqwPdQBpI%2BmdPE6daA4bTuxz2RHgOwfh42ophC8cGwoGIQxgRM71bBpcmgj%2BYm%2FX0RRkxXFXc1z97J5CiQPDDLXcf7KFGCfWm47cH5L2tSAdElVqIiBcTT9az7JD3RgBM7ubwanRcVjsIBTZkXElamjuU9MEFnqUQmIe9jEKNwWIimaBMZKMfzEhyb84BeQB%2F3XmJZClNm%2BNJyDrz4crIujtxNlEg%2B4hGK1gZNxIepeuXVvK07x%2F5kVCvhHabiC5XmWWmfd5Ethov8L2BC3LMAvgMXlu1l32Jh4LN3dyswHdSVg5JEVqa68rqWcXaLlsBmMpcq%2BesixPtt5l1875EFivHmJQ6obZ0zL8r1ZessidxET931maVk9tTaKztXaEMI3g7NAGOqUBWd%2F%2Fl9m2ov7ucrCOwC%2Bjn6aZKUkl7qBtk8G9IaIAFbYZJv9x1T4LH7ugvxzMsU4pkMCc%2FYXk0eDK1J8r48GzTEB%2FlbvCqUD%2FlJe2LD4SVJxYGyN7CWpFeW41wFPkUggXN678qe%2FIP%2FaWoFgPqZa%2FCvKzuSMv1hc0ygjc95FYQuYVjzFtSiT3CyZi7fR25uRjCv%2FhW9jmjxKxNup3VrSVgp%2BbNe0u&X-Amz-Signature=5ce5e6aaf2aad5b86a5d48f5799a219932a5f13afbaeab03f83c67d78aadf9a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







