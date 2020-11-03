Hooks.once("init", () => {
    console.log("Init");

    CONFIG.Combat.initiative = {
        formular: "@initiative.base", decimals: 0
    }

    Actors.unregisterSheet("core", ActorSheet)
    Actors.registerSheet("dark-eye-5", PlayerSheet, {
        types: ["player"], makeDefault: true
    });
});

Hooks.on("preCreateActor", (createData) => {
    if(createData.type == "player"){
        createData.token.vision = true;
        createData.token.actorLink = true;
    }
})