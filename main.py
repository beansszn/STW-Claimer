# Imports
from rich.console import Console
import asyncio
import httpx

# Initialize console
console = Console()

# Constants
AUTH_TOKEN = ""
ACCOUNT_ID = ""
BASE_URL = "https://fngw-mcp-gc-livefn.ol.epicgames.com/fortnite/api/game/v2"
URL_PATH = f"/profile/{ACCOUNT_ID}/client/PurchaseOrUpgradeHomebaseNode?profileId=campaign&rvn=-1"
NODE_IDS = [
    'HomebaseNode:questreward_buildingresourcecap',
    'HomebaseNode:questreward_buildingresourcecap2',
    'HomebaseNode:questreward_buildingresourcecap3',
    'HomebaseNode:questreward_buildingupgradelevel',
    'HomebaseNode:questreward_buildingupgradelevel2',
    'HomebaseNode:questreward_cannyvalley_squad_ssd1',
    'HomebaseNode:questreward_cannyvalley_squad_ssd2',
    'HomebaseNode:questreward_cannyvalley_squad_ssd3',
    'HomebaseNode:questreward_cannyvalley_squad_ssd4',
    'HomebaseNode:questreward_cannyvalley_squad_ssd5',
    'HomebaseNode:questreward_cannyvalley_squad_ssd6',
    'HomebaseNode:questreward_evolution',
    'HomebaseNode:questreward_evolution2',
    'HomebaseNode:questreward_evolution3',
    'HomebaseNode:questreward_evolution4',
    'HomebaseNode:questreward_expedition_dirtbike',
    'HomebaseNode:questreward_expedition_dirtbike2',
    'HomebaseNode:questreward_expedition_dirtbike3',
    'HomebaseNode:questreward_expedition_helicopter',
    'HomebaseNode:questreward_expedition_helicopter2',
    'HomebaseNode:questreward_expedition_helicopter3',
    'HomebaseNode:questreward_expedition_helicopter4',
    'HomebaseNode:questreward_expedition_propplane',
    'HomebaseNode:questreward_expedition_propplane2',
    'HomebaseNode:questreward_expedition_propplane3',
    'HomebaseNode:questreward_expedition_rowboat',
    'HomebaseNode:questreward_expedition_rowboat2',
    'HomebaseNode:questreward_expedition_rowboat3',
    'HomebaseNode:questreward_expedition_rowboat4',
    'HomebaseNode:questreward_expedition_speedboat',
    'HomebaseNode:questreward_expedition_speedboat2',
    'HomebaseNode:questreward_expedition_speedboat3',
    'HomebaseNode:questreward_expedition_speedboat4',
    'HomebaseNode:questreward_expedition_speedboat5',
    'HomebaseNode:questreward_expedition_truck',
    'HomebaseNode:questreward_expedition_truck2',
    'HomebaseNode:questreward_expedition_truck3',
    'HomebaseNode:questreward_expedition_truck4',
    'HomebaseNode:questreward_expedition_truck5',
    'HomebaseNode:questreward_feature_defenderlevelup',
    'HomebaseNode:questreward_feature_herolevelup',
    'HomebaseNode:questreward_feature_reperk',
    'HomebaseNode:questreward_feature_researchsystem',
    'HomebaseNode:questreward_feature_skillsystem',
    'HomebaseNode:questreward_feature_survivorlevelup',
    'HomebaseNode:questreward_feature_survivorslotting',
    'HomebaseNode:questreward_feature_traplevelup',
    'HomebaseNode:questreward_feature_weaponlevelup',
    'HomebaseNode:questreward_herosupport_slot',
    'HomebaseNode:questreward_herotactical_slot',
    'HomebaseNode:questreward_homebase_defender',
    'HomebaseNode:questreward_homebase_defender2',
    'HomebaseNode:questreward_homebase_defender3',
    'HomebaseNode:questreward_homebase_defender4',
    'HomebaseNode:questreward_homebase_defender5',
    'HomebaseNode:questreward_mission_defender',
    'HomebaseNode:questreward_mission_defender2',
    'HomebaseNode:questreward_mission_defender3',
    'HomebaseNode:questreward_newfollower1_slot',
    'HomebaseNode:questreward_newfollower2_slot',
    'HomebaseNode:questreward_newfollower3_slot',
    'HomebaseNode:questreward_newfollower4_slot',
    'HomebaseNode:questreward_newfollower5_slot',
    'HomebaseNode:questreward_newheroloadout2_dummy',
    'HomebaseNode:questreward_newheroloadout3_dummy',
    'HomebaseNode:questreward_newheroloadout4_dummy',
    'HomebaseNode:questreward_newheroloadout5_dummy',
    'HomebaseNode:questreward_newheroloadout6_dummy',
    'HomebaseNode:questreward_newheroloadout7_dummy',
    'HomebaseNode:questreward_newheroloadout8_dummy',
    'HomebaseNode:questreward_pickaxe',
    'HomebaseNode:questreward_plankerton_squad_ssd1',
    'HomebaseNode:questreward_plankerton_squad_ssd2',
    'HomebaseNode:questreward_plankerton_squad_ssd3',
    'HomebaseNode:questreward_plankerton_squad_ssd4',
    'HomebaseNode:questreward_plankerton_squad_ssd5',
    'HomebaseNode:questreward_plankerton_squad_ssd6',
    'HomebaseNode:questreward_recyclecollection',
    'HomebaseNode:questreward_stonewood_squad_ssd1',
    'HomebaseNode:questreward_stonewood_squad_ssd2',
    'HomebaseNode:questreward_stonewood_squad_ssd3',
    'HomebaseNode:questreward_stonewood_squad_ssd4',
    'HomebaseNode:questreward_stonewood_squad_ssd5',
    'HomebaseNode:questreward_stonewood_squad_ssd6',
    'HomebaseNode:questreward_teamperk_slot1',
    'HomebaseNode:questreward_twinepeaks_squad_ssd1',
    'HomebaseNode:questreward_twinepeaks_squad_ssd2',
    'HomebaseNode:questreward_twinepeaks_squad_ssd3',
    'HomebaseNode:questreward_twinepeaks_squad_ssd4',
    'HomebaseNode:questreward_twinepeaks_squad_ssd5',
    'HomebaseNode:questreward_twinepeaks_squad_ssd6',
]

# Headers for the request
HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# COUNTERS
CLAIMED = 0
FAILED = 0

# Operation
async def claim_node(client, node_id):
    global CLAIMED, FAILED
    url = f"{BASE_URL}{URL_PATH}&nodeId={node_id}"
    try:
        response = await client.post(url, json={'nodeId': node_id})
        data = response.json()

        if response.status_code == 200:
            CLAIMED += 1
            return f"[green bold]✅ Claimed: [italic white]{node_id}"
        
        elif data.get("errorCode") == "errors.com.epicgames.fortnite.item_not_found":
            FAILED += 1
            return f"[yellow bold]⚠️  Node already claimed: [italic white]{node_id}"
        else:
            FAILED += 1
            return f"[red bold]❌ Failed: {node_id}: {data.get('errorMessage', 'Unknown error')}"
    
    except Exception as e:
        return f"[red bold]❌ Exception for {node_id}: {e}"

async def main():
    async with httpx.AsyncClient(headers=HEADERS, timeout=10) as client:
        tasks = [claim_node(client, node_id) for node_id in NODE_IDS]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    with console.status("[bold green]Claiming STW nodes...", spinner="dots"):
        results = asyncio.run(main())
        for result in results:
            console.print(result)
        console.print(f"\n[bold green]✅ {CLAIMED} [italic]({(CLAIMED / len(NODE_IDS)) * 100:.2f}%)\n[bold red]❌ {FAILED} [italic]({(FAILED / len(NODE_IDS)) * 100:.2f}%)")
    console.print("\n[bold magenta]Finished claiming nodes!")
    
