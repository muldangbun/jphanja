const fs = require('fs');

const romajiList = [
    "kani ga iroiro kangaeta ageku tokoya o hajimemashita",
    "kani no kangae to shite wa oodeki de arimashita",
    "tokoro de kani wa tokoya to iu shoubai wa taihen hima na mono da na to omoimashita",
    "to moushimasu no wa hitori mo okyakusan ga konai kara de arimasu",
    "sokode kani no tokoyasan wa hasami o motte umippata ni yatte ikimashita",
    "soko ni wa tako ga hirune o shite imashita",
    "moshi moshi takosan to kani wa yobikakemashita",
    "tako wa me o samashite nan da to iimashita",
    "tokoya desu ga goyou wa arimasen ka",
    "yoku goran yo watashi no atama ni ke ga aru ka dou ka",
    "kani wa tako no atama o yoku mimashita",
    "naruhodo ke wa hitosuji mo naku tsurunko de arimashita",
    "ikura kani ga jouzu na tokoya demo ke no nai atama o karu koto wa dekimasen",
    "kani wa sokode yama e yatte ikimashita",
    "yama ni wa tanuki ga hirune o shite imashita",
    "moshi moshi tanukisan",
    "tanuki wa me o samashite nan da to iimashita",
    "tokoya desu ga goyou wa arimasen ka",
    "tanuki wa itazura ga suki na kemono desu kara yokunai koto o kangaemashita",
    "yoroshii katte moraou tokoro de hitotsu yakusoku shite kurenakya ikenai",
    "to iu no wa watashi no ato de watashi no otousan no ke mo katte moraitai no sa",
    "hei oyasui koto desu",
    "sokode kani no ude o furuu toki ga kimashita",
    "chokkin chokkin chokkin",
    "tokoroga kani to iu mono wa amari ookina mono de wa arimasen",
    "kani to kurabetara tanuki wa tondemonaku ookina mono de arimasu",
    "sono ue tanuki to iu mono wa karadajuu ga kemukujara de arimasu",
    "desukara shigoto wa nakanaka hakadorimasen",
    "kani wa kuchi kara awa o fuite isshoukenmei hasami o tsukaimashita",
    "soshite mikka kakatte yatto no koto shigoto wa owarimashita",
    "ja yakusoku dakara watashi no otousan no ke mo katte kure tamae",
    "otousan to iu no wa dono kurai ookina kata desu ka",
    "ano yama kurai aru ka ne",
    "kani wa menkuraimashita",
    "sonna ni ookikute wa totemo jibun hitori de wa maniawanu to omoimashita",
    "sokode kani wa jibun no kodomotachi o mina tokoya ni shimashita",
    "kodomo bakari ka mago mo hiko mo umarete kuru kani wa mina tokoya ni shimashita",
    "sore de watakushitachi ga michibata ni miukeru honni chiisana kani de saemo chanto hasami o motte imasu"
];

let data = JSON.parse(fs.readFileSync('kaninotokoya.JSON', 'utf8'));

for (let i = 0; i < data.length; i++) {
    if (romajiList[i]) {
        data[i].romaji = romajiList[i];
    }
}

fs.writeFileSync('kaninotokoya.JSON', JSON.stringify(data, null, 4));
console.log('Romaji spaces successfully applied.');

