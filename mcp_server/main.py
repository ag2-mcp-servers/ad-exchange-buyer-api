# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T00:37:48+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Path, Query
from pydantic import conint

from models import (
    Account,
    AccountId,
    AccountsList,
    AddOrderDealsRequest,
    AddOrderDealsResponse,
    AddOrderNotesRequest,
    AddOrderNotesResponse,
    Alt,
    BillingInfo,
    BillingInfoList,
    Budget,
    BuyerCreativeId,
    CreateOrdersRequest,
    CreateOrdersResponse,
    Creative,
    CreativeDealIds,
    CreativesList,
    DealsStatusFilter,
    DeleteOrderDealsRequest,
    DeleteOrderDealsResponse,
    EditAllOrderDealsRequest,
    EditAllOrderDealsResponse,
    GetOffersResponse,
    GetOrderDealsResponse,
    GetOrderNotesResponse,
    GetOrdersResponse,
    GetPublisherProfilesByAccountIdResponse,
    OpenAuctionStatusFilter,
    PerformanceReportList,
    PretargetingConfig,
    PretargetingConfigList,
    Product,
    Proposal,
    UpdateAction,
    UpdatePrivateAuctionProposalRequest,
)

app = MCPProxy(
    contact={'name': 'Google', 'url': 'https://google.com', 'x-twitter': 'youtube'},
    description='Accesses your bidding-account information, submits creatives for validation, finds available direct deals, and retrieves performance reports.',
    license={
        'name': 'Creative Commons Attribution 3.0',
        'url': 'http://creativecommons.org/licenses/by/3.0/',
    },
    termsOfService='https://developers.google.com/terms/',
    title='Ad Exchange Buyer API',
    version='v1.4',
    servers=[{'url': 'https://www.googleapis.com/adexchangebuyer/v1.4'}],
)


@app.get(
    '/accounts',
    description=""" Retrieves the authenticated user's list of accounts. """,
    tags=['account_management', 'public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_accounts_list(
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/accounts/{id}',
    description=""" Gets one account by ID. """,
    tags=['public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_accounts_get(
    id: int,
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/accounts/{id}',
    description=""" Updates an existing account. This method supports patch semantics. """,
    tags=['account_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_accounts_patch(
    id: int,
    confirm_unsafe_account_change: Optional[bool] = Query(
        None, alias='confirmUnsafeAccountChange'
    ),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Account = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/accounts/{id}',
    description=""" Updates an existing account. """,
    tags=['account_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_accounts_update(
    id: int,
    confirm_unsafe_account_change: Optional[bool] = Query(
        None, alias='confirmUnsafeAccountChange'
    ),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Account = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/billinginfo',
    description=""" Retrieves a list of billing information for all accounts of the authenticated user. """,
    tags=['account_management', 'public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_billing_info_list(
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/billinginfo/{accountId}',
    description=""" Returns the billing information for one account specified by account ID. """,
    tags=['account_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_billing_info_get(
    account_id: int = Path(..., alias='accountId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/billinginfo/{accountId}/{billingId}',
    description=""" Returns the budget information for the adgroup specified by the accountId and billingId. """,
    tags=['billing_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_budget_get(
    account_id: str = Path(..., alias='accountId'),
    billing_id: str = Path(..., alias='billingId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/billinginfo/{accountId}/{billingId}',
    description=""" Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request. This method supports patch semantics. """,
    tags=['billing_handling', 'budget_tracking'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_budget_patch(
    account_id: str = Path(..., alias='accountId'),
    billing_id: str = Path(..., alias='billingId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Budget = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/billinginfo/{accountId}/{billingId}',
    description=""" Updates the budget amount for the budget of the adgroup specified by the accountId and billingId, with the budget amount in the request. """,
    tags=['billing_handling', 'budget_tracking'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_budget_update(
    account_id: str = Path(..., alias='accountId'),
    billing_id: str = Path(..., alias='billingId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Budget = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/creatives',
    description=""" Retrieves a list of the authenticated user's active creatives. A creative will be available 30-40 minutes after submission. """,
    tags=['creative_asset_management', 'deal_management', 'ad_deal_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_list(
    account_id: Optional[AccountId] = Query(None, alias='accountId'),
    buyer_creative_id: Optional[BuyerCreativeId] = Query(None, alias='buyerCreativeId'),
    deals_status_filter: Optional[DealsStatusFilter] = Query(
        None, alias='dealsStatusFilter'
    ),
    max_results: Optional[conint(ge=1, le=1000)] = Query(None, alias='maxResults'),
    open_auction_status_filter: Optional[OpenAuctionStatusFilter] = Query(
        None, alias='openAuctionStatusFilter'
    ),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/creatives',
    description=""" Submit a new creative. """,
    tags=['creative_asset_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_insert(
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Creative = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/creatives/{accountId}/{buyerCreativeId}',
    description=""" Gets the status for a single creative. A creative will be available 30-40 minutes after submission. """,
    tags=['account_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_get(
    account_id: int = Path(..., alias='accountId'),
    buyer_creative_id: str = Path(..., alias='buyerCreativeId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/creatives/{accountId}/{buyerCreativeId}/addDeal/{dealId}',
    description=""" Add a deal id association for the creative. """,
    tags=['deal_management', 'ad_deal_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_add_deal(
    account_id: int = Path(..., alias='accountId'),
    buyer_creative_id: str = Path(..., alias='buyerCreativeId'),
    deal_id: str = Path(..., alias='dealId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/creatives/{accountId}/{buyerCreativeId}/listDeals',
    description=""" Lists the external deal ids associated with the creative. """,
    tags=['account_management', 'creative_asset_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_list_deals(
    account_id: int = Path(..., alias='accountId'),
    buyer_creative_id: str = Path(..., alias='buyerCreativeId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/creatives/{accountId}/{buyerCreativeId}/removeDeal/{dealId}',
    description=""" Remove a deal id associated with the creative. """,
    tags=['deal_management', 'ad_deal_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_creatives_remove_deal(
    account_id: int = Path(..., alias='accountId'),
    buyer_creative_id: str = Path(..., alias='buyerCreativeId'),
    deal_id: str = Path(..., alias='dealId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/performancereport',
    description=""" Retrieves the authenticated user's list of performance metrics. """,
    tags=['performance_analysis'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_performance_report_list(
    account_id: str = Query(..., alias='accountId'),
    end_date_time: str = Query(..., alias='endDateTime'),
    start_date_time: str = Query(..., alias='startDateTime'),
    max_results: Optional[conint(ge=1, le=1000)] = Query(None, alias='maxResults'),
    page_token: Optional[str] = Query(None, alias='pageToken'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/pretargetingconfigs/{accountId}',
    description=""" Retrieves a list of the authenticated user's pretargeting configurations. """,
    tags=['account_management', 'public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_list(
    account_id: str = Path(..., alias='accountId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/pretargetingconfigs/{accountId}',
    description=""" Inserts a new pretargeting configuration. """,
    tags=['pretargeting_setup'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_insert(
    account_id: str = Path(..., alias='accountId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: PretargetingConfig = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/pretargetingconfigs/{accountId}/{configId}',
    description=""" Deletes an existing pretargeting config. """,
    tags=['account_management', 'public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_delete(
    account_id: str = Path(..., alias='accountId'),
    config_id: str = Path(..., alias='configId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/pretargetingconfigs/{accountId}/{configId}',
    description=""" Gets a specific pretargeting configuration """,
    tags=['account_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_get(
    account_id: str = Path(..., alias='accountId'),
    config_id: str = Path(..., alias='configId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/pretargetingconfigs/{accountId}/{configId}',
    description=""" Updates an existing pretargeting config. This method supports patch semantics. """,
    tags=['pretargeting_setup'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_patch(
    account_id: str = Path(..., alias='accountId'),
    config_id: str = Path(..., alias='configId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: PretargetingConfig = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/pretargetingconfigs/{accountId}/{configId}',
    description=""" Updates an existing pretargeting config. """,
    tags=['pretargeting_setup'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pretargeting_config_update(
    account_id: str = Path(..., alias='accountId'),
    config_id: str = Path(..., alias='configId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: PretargetingConfig = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/privateauction/{privateAuctionId}/updateproposal',
    description=""" Update a given private auction proposal """,
    tags=[
        'marketplace_operations',
        'proposal_handling',
        'proposal_revision_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplaceprivateauction_updateproposal(
    private_auction_id: str = Path(..., alias='privateAuctionId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: UpdatePrivateAuctionProposalRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/products/search',
    description=""" Gets the requested product. """,
    tags=['public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_products_search(
    pql_query: Optional[str] = Query(None, alias='pqlQuery'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/products/{productId}',
    description=""" Gets the requested product by id. """,
    tags=['product_dataset_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_products_get(
    product_id: str = Path(..., alias='productId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/insert',
    description=""" Create the given list of proposals """,
    tags=['marketplace_operations', 'product_dataset_management', 'ad_deal_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_insert(
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: CreateOrdersRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/proposals/search',
    description=""" Search for proposals using pql query """,
    tags=['public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_search(
    pql_query: Optional[str] = Query(None, alias='pqlQuery'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/proposals/{proposalId}',
    description=""" Get a proposal given its id """,
    tags=[
        'proposal_handling',
        'marketplace_operations',
        'proposal_revision_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_get(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/proposals/{proposalId}/deals',
    description=""" List all the deals for a given proposal """,
    tags=[
        'proposal_handling',
        'marketplace_operations',
        'proposal_revision_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacedeals_list(
    proposal_id: str = Path(..., alias='proposalId'),
    pql_query: Optional[str] = Query(None, alias='pqlQuery'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/{proposalId}/deals/delete',
    description=""" Delete the specified deals from the proposal """,
    tags=['deal_management', 'proposal_handling', 'ad_deal_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacedeals_delete(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: DeleteOrderDealsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/{proposalId}/deals/insert',
    description=""" Add new deals for the specified proposal """,
    tags=[
        'marketplace_operations',
        'proposal_handling',
        'deal_management',
        'ad_deal_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacedeals_insert(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: AddOrderDealsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/{proposalId}/deals/update',
    description=""" Replaces all the deals in the proposal with the passed in deals """,
    tags=[
        'marketplace_operations',
        'proposal_handling',
        'deal_management',
        'ad_deal_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacedeals_update(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: EditAllOrderDealsRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/proposals/{proposalId}/notes',
    description=""" Get all the notes associated with a proposal """,
    tags=['proposal_handling', 'marketplace_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacenotes_list(
    proposal_id: str = Path(..., alias='proposalId'),
    pql_query: Optional[str] = Query(None, alias='pqlQuery'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/{proposalId}/notes/insert',
    description=""" Add notes to the proposal """,
    tags=['note_handling', 'proposal_handling'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_marketplacenotes_insert(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: AddOrderNotesRequest = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/proposals/{proposalId}/setupcomplete',
    description=""" Update the given proposal to indicate that setup has been completed. """,
    tags=['proposal_handling', 'marketplace_operations'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_setupcomplete(
    proposal_id: str = Path(..., alias='proposalId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/proposals/{proposalId}/{revisionNumber}/{updateAction}',
    description=""" Update the given proposal. This method supports patch semantics. """,
    tags=[
        'marketplace_operations',
        'proposal_handling',
        'proposal_revision_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_patch(
    proposal_id: str = Path(..., alias='proposalId'),
    revision_number: str = Path(..., alias='revisionNumber'),
    update_action: UpdateAction = Path(..., alias='updateAction'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Proposal = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.put(
    '/proposals/{proposalId}/{revisionNumber}/{updateAction}',
    description=""" Update the given proposal """,
    tags=[
        'marketplace_operations',
        'proposal_handling',
        'proposal_revision_management',
    ],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_proposals_update(
    proposal_id: str = Path(..., alias='proposalId'),
    revision_number: str = Path(..., alias='revisionNumber'),
    update_action: UpdateAction = Path(..., alias='updateAction'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
    body: Proposal = None,
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/publisher/{accountId}/profiles',
    description=""" Gets the requested publisher profile(s) by publisher accountId. """,
    tags=['account_management', 'public_profile_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
        UnsuportedSecurityStub(name="None"),
    ],
)
def adexchangebuyer_pubprofiles_list(
    account_id: int = Path(..., alias='accountId'),
    alt: Optional[Alt] = None,
    fields: Optional[str] = None,
    key: Optional[str] = None,
    oauth_token: Optional[str] = None,
    pretty_print: Optional[bool] = Query(None, alias='prettyPrint'),
    quota_user: Optional[str] = Query(None, alias='quotaUser'),
    user_ip: Optional[str] = Query(None, alias='userIp'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
