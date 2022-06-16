<head>
<meta charset="UTF-8">
<title>Société à responsabilité limitée (SRL) Belge Minimale pour  </title>
<style>
body {
    background: #fafafa;
    color: #222;
    font-family: "HelveticaNeue", "Helvetica Neue", Helvetica, Arial, sans-serif;
    font-size: 15px;
    line-height: 1.5;
    margin-top: 0;
}
@media screen and (min-width: 800px) {
    body {
        margin: 0 45px 30px 45px;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
}
blockquote {
    margin: 0;
    border-left: 5px solid #7a7a7a;
    background-color: #eee;
    padding: 30px;
}
h1, h2, h3, h4, h5, h6 {
    margin: 20px 0;
}
td {
    padding: 4px;
}
tr td:nth-child(2), tr td:nth-child(3), tr td:nth-child(4), tr td:nth-child(7) {
    text-align: right;
}
body > p:first-of-type {
    margin-top: 0;
}
body > h1:first-of-type {
    margin-top: 0;
}
.hide {
    display: none;
}
</style>
<script>
window.addEventListener('DOMContentLoaded', function() {
    for(var n of document.querySelectorAll("li > a")) {
        if(!n.name || !n.name.includes("toc"))
            continue;
        var t = n.nextSibling;
        t.parentNode.insertBefore(document.createTextNode(" "),t);
        var a = document.createElement("a");
        a.name = "show";
        a.href = "#";
        a.innerHTML = " 📖";
        t.parentNode.insertBefore(a,t);
        var span = document.createElement("span");
        span.className = "hide";
        span.appendChild(t.cloneNode());
        t.replaceWith(span);
        //document.querySelectorAll("li > a")[10].nextSibling
    }
    document.addEventListener('click',function(e) {
        var n=e.target;
        if(!n.name || !n.name.includes("show"))
            return;
        var t = n.nextSibling;
        if(t.classList.contains("hide")) {
            t.className = "";
        } else {
            t.className = "hide";
        }
        e.preventDefault();
    });
});
</script>
</head>
<body>

<a href="https://github.com/antonylesuisse/belgium-srl"><img loading="lazy" width="149" height="149" src="https://github.blog/wp-content/uploads/2008/12/forkme_right_gray_6d6d6d.png?resize=149%2C149" alt="Fork me on GitHub" style="float: right;"></a>

# Société à responsabilité limitée (SRL) Belge Minimale

Derniere date de modification 2022-02-12.

## Frais et demarches de constitution 484,40 EUR

1. Plan financier.
2. Acte de constitution et publication au Moniteur Belge. 393,90 EUR
3. Inscription à la Banque-Carrefour des Entreprises (BCE). 90,50 EUR
4. Demande d'identification à la TVA.
5. Registre d'actionnaire.

## 1. Plan financier

Plan financier d'au moins deux ans, pour justifier le montant des capitaux propres, à remettre au notaire lors de l'acte de constitution. Les 2 permieres années, le juge peut lever la responsibilité limitée, en cas de faillite, si le plan était inadéquois.<a href="http://www.ejustice.just.fgov.be/eli/loi/2019/03/23/2019A40586/justel">Code des societés Art. 5:4</a>.

1. <a name="5:4.1-toc" href="#5:4.1">Description (5:4 1°)</a> une description précise de l'activité projetée;
2. <a name="5:4.2-toc" href="#5:4.2">Sources (5:4 2°)</a> un aperçu de toutes les sources de financement à la constitution en ce compris, le cas échéant, la mention des garanties fournies à cet égard;
3. <a name="5:3.3-toc" href="#5:3.3">Bilan (5:3 3°)</a> un bilan d'ouverture établi conformément au schéma visé à l'article 3:3, ainsi que des bilans projetés après douze et vingt-quatre mois;
4. <a name="5:3.4-toc" href="#5:3.4">Résultat (5:3 4°)</a> un compte de résultats projeté après douze et vingt-quatre mois, établi conformément au schéma visé à l'article 3:3;
5. <a name="5:3.5-toc" href="#5:3.5">Budget (5:3 5°)</a> un budget des revenus et dépenses projetés pour une période d'au moins deux ans à compter de la constitution;
6. <a name="5:3.6-toc" href="#5:3.6">Hypothèses (5:3 6°)</a> une description des hypothèses retenues lors de l'estimation du chiffre d'affaires et de la rentabilité prévus;
7. <a name="5:3.7-toc" href="#5:3.7">Expert (optionel) (5:3 7°)</a> le cas échéant, le nom de l'expert externe qui a apporté son assistance lors de l'établissement du plan financier.

Template du business plan minimaliste:

> <a href="srl_bp.docx" style="float: right;">⬇️  srl_bp.docx</a>
> <br style="clear: right;">
> Description: Prestation de consultance en informatique, développement de logiciel mesure <a name="5:4.1" href="#5:4.1-toc">(5:4 1°)</a>, facturé en régie à un tarif de 300EUR/jour 4 jours par mois <a name="5:3.6" href="#5:3.6-toc">(5:3 6°)</a>, financé par capitaux propres et compte courant adminstrateur <a name="5:4.2" href="#5:4.2-toc">(5:4 2°)</a>. 
> 
> Bilan <a name="5:3.3" href="#5:3.3-toc">(5:3 3°)</a>, Résultats <a name="5:3.4" href="#5:3.4-toc">(5:3 4°)</a> et Budget <a name="5:3.5" href="#5:3.5-toc">(5:3 5°)</a>.
> 
> <table style="border: 1px solid #999;">
> <tr> <td>Montant en EUR          </td> <th>Constitution</th> <th>Année +1</th> <th>Année +2</th> </tr>
> <tr> <th>Actifs                  </th> <td>            </td> <td>        </td> <td>        </td> </tr>
> <tr> <td>200 Etablissement       </td> <td>         500</td> <td>     500</td> <td>     500</td> </tr>
> <tr> <td>416 Capital à recevoir  </td> <td>         340</td> <td>        </td> <td>        </td> </tr>
> <tr> <td>500 Banque              </td> <td>            </td> <td>    6340</td> <td>   12340</td> </tr>
> <tr> <th>Passif                  </th> <td>            </td> <td>        </td> <td>        </td> </tr>
> <tr> <td>100 Capital appelé      </td> <td>         500</td> <td>     840</td> <td>     840</td> </tr>
> <tr> <td>100 Capital non appelé  </td> <td>         340</td> <td>        </td> <td>        </td> </tr>
> <tr> <td>130 Reserve             </td> <td>            </td> <td>      84</td> <td>      84</td> </tr>
> <tr> <td>140 Bénéfice reporté    </td> <td>            </td> <td>    5916</td> <td>   11916</td> </tr>
> <tr> <th>Résultats               </th> <td>            </td> <td>        </td> <td>        </td> </tr>
> <tr> <td>710 Consultance         </td> <td>            </td> <td>   12000</td> <td>   12000</td> </tr>
> <tr> <td>611 Internet            </td> <td>            </td> <td>    1000</td> <td>    1000</td> </tr>
> <tr> <td>612 Cloud Hosting       </td> <td>            </td> <td>    1000</td> <td>    1000</td> </tr>
> <tr> <td>613 Fournitures         </td> <td>            </td> <td>    1000</td> <td>    1000</td> </tr>
> <tr> <td>620 Remuneration        </td> <td>            </td> <td>    3000</td> <td>    3000</td> </tr>
> <tr> <th>Cashflow Budget         </th> <td>            </td> <td>        </td> <td>        </td> </tr>
> <tr> <td>Liquiditées             </td> <td>           0</td> <td>   +6340</td> <td>   +6000</td> </tr>
> </table>
> 

## 2. Acte de constitution

Couts total 393,90 EUR à payer au notaire.

- Honoraire du notaire 42,18 EUR: <a href="https://www.ejustice.just.fgov.be/cgi_loi/change_lg_2.pl?language=fr&nm=1950121605&la=F">Loi du 16 Décembre 1950. Art. 17. 74 2°, Art. 5</a> Bareme L soit 0.57% du capital avec un minimum de 42,18 EUR.
- Taxe "Droits d'écriture" 95 EUR: <a href="https://www.ejustice.just.fgov.be/cgi_loi/change_lg_2.pl?language=fr&nm=1927030201&la=F">Loi du 2 Mars 1927. Art. 4</a>.
- Taxe "Droits d’enregistrement au SPF Finance" 50 EUR: <a href="https://wallex.wallonie.be/eli/loi-decret/1939/11/29/193913002">Code des droits d'enregistrement, d'hypothèque et greffe du 29 novembre 1939. Référence non trouvée.</a>.
- Publication au Moniteur Belge 231,72 EUR <a href="http://www.ejustice.just.fgov.be/eli/loi/2019/03/23/2019A40586/justel#Art.2:13">Code des societés Art. 2:13</a>, <a href="https://www.e-greffe.be/evzw/fr/homepagee-greffe">e-greffe</a>.

Voici un template de projet d'acte de constitution, le plus court et minimaliste possible pour une SRL, en respectant, à la lettre, <a href="http://www.ejustice.just.fgov.be/eli/loi/2019/03/23/2019A40586/justel#Art.5:9">l'article 5:12 du Code de Sociétés Belge</a>:

Outre les données comprises dans l'extrait destiné à la publication en vertu de <a href="http://www.ejustice.just.fgov.be/eli/loi/2019/03/23/2019A40586/justel#Art.2:8">l'article 2:8, § 2</a>,

- <a name="2:8.2.1-toc" href="#2:8.2.1">Dénomination (2:8 § 2 1°)</a>: la forme légale de la société, sa dénomination et l'indication de la région dans laquelle le siège de la société est établi;
- <a name="2:8.2.2-toc" href="#2:8.2.2">Siége (2:8 § 2 2°)</a>: la désignation précise de l'adresse à laquelle le siège de la société est établi et, le cas échéant, l'adresse électronique et le site internet de la société;
- <a name="2:8.2.3-toc" href="#2:8.2.3">Durée (optionel) (2:8 § 2 3°)</a>: la durée de la société lorsqu'elle n'est pas illimitée;
- <a name="2:8.2.4-toc" href="#2:8.2.4">Actionnaires (2:8 § 2 4°)</a>: les nom, prénom et domicile des associés solidaires, des fondateurs et des associés ou actionnaires qui n'ont pas encore libéré leur apport; dans ce dernier cas, l'extrait contient pour chaque associé ou actionnaire le montant qui reste à libérer;
- <a name="2:8.2.5-toc" href="#2:8.2.5">Capital (2:8 § 2 5°)</a>: le cas échéant, le montant du capital et le montant du capital autorisé;
- <a name="2:8.2.6-toc" href="#2:8.2.6">Apports (2:8 § 2 6°)</a>: les apports des fondateurs [1 et des souscripteurs]1, le montant pour lequel les apports sont libérés, le cas échéant, les conclusions du rapport du réviseur d'entreprises concernant les apports en nature, et, en outre, pour la société en commandite, le montant des valeurs libérées ou à libérer par les associés commanditaires;
- <a name="2:8.2.7-toc" href="#2:8.2.7">Exercice (2:8 § 2 7°)</a>: le début et la fin de chaque exercice social;
- <a name="2:8.2.8-toc" href="#2:8.2.8">Bénéfices (2:8 § 2 8°)</a>: les dispositions relatives à la constitution des réserves, à la répartition des bénéfices et du boni de liquidation de la société;
- <a name="2:8.2.9-toc" href="#2:8.2.9">Administration (2:8 § 2 9°)</a>: le mode de nomination et de cessation de fonctions des personnes autorisées à administrer et à représenter la société, l'étendue de leurs pouvoirs et les modalités d'exercice de ces derniers soit séparément, soit conjointement, soit en collège, et le cas échéant, l'étendue des pouvoirs des membres du conseil de surveillance et les modalités d'exercice de ces derniers;
- <a name="2:8.2.10-toc" href="#2:8.2.10">Administrateur (2:8 § 2 10°)</a>: l'identité des personnes autorisées à administrer et à représenter la société et, le cas échéant, des membres du conseil de surveillance et du commissaire;
- <a name="2:8.2.11-toc" href="#2:8.2.11">But (optionel) (2:8 § 2 11°)</a>: le cas échéant, la description précise du ou des buts qu'elle poursuit en plus du but de distribuer ou procurer à ses associés un avantage patrimonial direct ou indirect;
- <a name="2:8.2.12-toc" href="#2:8.2.12">Objet (2:8 § 2 12°)</a> la désignation de l'objet de la société;
- <a name="2:8.2.13-toc" href="#2:8.2.13">Assemblée (2:8 § 2 13°)</a> les lieu, jour et heure de l'assemblée générale ordinaire des associés ou actionnaires ainsi que les conditions d'admission et d'exercice du droit de vote;
- <a name="2:8.2.14-toc" href="#2:8.2.14">Noms (2:8 § 2 14°)</a> les nom, prénom et domicile ou, pour les personnes morales, leurs dénomination, forme légale, numéro d'entreprise et siège, des mandataires, les données prévues par le présent code ainsi que les dispositions pertinentes des procurations sous seing privé ou authentique;

l'acte constitutif mentionne les données suivantes:

- (5:12 1°) le respect des conditions visées aux articles 5:3, 5:5 et 5:8;
    - <a name="5:3-toc" href="#5:3"> Capitaux suffisant (5:3)</a>: Les fondateurs veillent à ce que la société à responsabilité limitée dispose lors de sa constitution de capitaux propres qui, compte tenu des autres sources de financement, sont suffisants à la lumière de l'activité projetée.
    - <a name="5:5-toc" href="#5:5">Souscription (5:5)</a>: Les actions émises par la société doivent être intégralement et, nonobstant toute disposition contraire, inconditionnellement souscrites.
    - <a name="5:8-toc" href="#5:8">Libération (5:8 </a>: Sauf disposition contraire dans l'acte constitutif, tous les apports sont intégralement libérés dès la constitution.
- <a name="5:12.2-toc" href="#5:12.2">Banque (optionel) (5:12 2°)</a>: l'organisme dépositaire des apports à libérer en numéraire conformément à l'article 5:9;
- <a name="5:12.3-toc" href="#5:12.3">Organes (optionel) (5:12 3°)</a>: les règles, dans la mesure où elles ne résultent pas de la loi, qui déterminent le nombre et le mode de désignation des membres des organes chargés de l'administration ou, le cas échéant, de la gestion journalière, de la représentation à l'égard des tiers ainsi que la répartition des compétences entre ces organes;
- <a name="5:12.4-toc" href="#5:12.4">Actions (5:12 4°)</a>: le nombre des actions, ainsi que, le cas échéant, les restrictions en matière de cession et, s'il existe différentes classes d'actions, les mêmes données et les droits par classe;
- <a name="5:12.5-toc" href="#5:12.5">Nature (optionel) (5:12 5°)</a>: l'indication de chaque apport en nature, le nom de l'apporteur, le nombre d'actions émises en contrepartie de chaque apport, le cas échéant, le nom du réviseur d'entreprises et les conclusions de son rapport ainsi que, le cas échéant, les conditions auxquelles l'apport est fait;
- <a name="5:12.6-toc" href="#5:12.6">Avantages (optionel) (5:12 6°)</a>: la nature et consistance des avantages particuliers attribués à chacun des fondateurs, ou à toute personne qui a participé directement ou indirectement à la constitution de la société;
- <a name="5:12.7-toc" href="#5:12.7">Frais (5:12 7°)</a>: le montant total, au moins approximatif, de tous les frais, dépenses et rémunérations ou charges, sous quelque forme que ce soit, qui incombent à la société ou qui sont mis à sa charge à raison de sa constitution;
- <a name="5:12.4-toc" href="#5:12.4">Hypothéques (optionel) (5:12 8°)</a>: les charges hypothécaires ou les nantissements grevant les biens apportés.


> <a href="srl_acte.docx" style="float: right;">⬇️  srl_acte.docx</a>
> <br style="clear: right;">
> Le **[Date: 6 décembre 2020]**, ont comparu, par vidéoconférence devant Maître **[NOTAIRE: Charles Stasse, Notaire à Bruxelles]**, exerçant sa fonction dans la société **[NOTAIRE-COMPANY: Notaire Partners]** ayant son siège à **[NOTAIRE-SIEGE: 50 avenue Louise, 1050 Bruxelles]**.
>
> - Monsieur **[NOM1: Dupont Pierre André Jacques]**, né à **[BIRTHPLACE1: Bruxelles]** le **[BIRTHDATE1: 1 janvier 2001]**, domicilié **[ADRESSE1: rue du Labrador 26, 1000 Bruxelles]**, inscrit au registre national avec le numéro **[REGNAT1: 010101-123-12]** <a name="2:8.2.14" href="#2:8.2.14-toc">(2:8 § 2 14°)</a>.
>
> Le(s) comparant(s) declare(nt):
>
> - confirmer que le notaire a lu tout ce qui précède dans sa totalité.
> - déclarer que ses données d'identité sont complètes et correctes.
> - déclarer être capable et compétent pour accomplir les actes juridiques constatés dans cet acte et ne pas être sous l'effet d'une mesure qui entraîne une incapacité.
>
> Le notaire soussigné certifie les nom, prénoms, lieu et date de naissance du comparant au vu des pièces officielles requises par la loi.
>
> ### Fondateurs
>
> Le(s) comparant(s) déclare(nt) que les actions sont souscrites en espèces par les fondateurs, au sens du Code des sociétés et associations, comme suit <a name="2:8.2.4" href="#2:8.2.4-toc">(2:8 § 2 4°)</a>, <a name="2:8.2.6" href="#2:8.2.6-toc">(2:8 § 2 6°)</a>:
>
> - par Monsieur Antony Lesuisse, à hauteur de **[ACTIONS1: huit cent quarante 840]** actions pour un apport de **[ACTIONS2: huit cent quarante euros (€ 840,00)]**.
>
> Il(s) déclare(nt) qu’en application de la faculté prévue à l’article 5:8 du Code des sociétés et des associations, aucun versement ne doit encore être effectué sur les actions au moment de la constitution.
>
> Les capitaux propres de départ sont d'un montant de **huit cent quarante euros [ACTIONS2: 840] EUR** <a name="2:8.2.5" href="#2:8.2.5-toc">(2:8 § 2 5°)</a>.
>
> Le(s) fondateur(s) a(ont) remis son plan financier, qui justifie les capitaux propres de départ de la société, au notaire.
>
> Le notaire les a informés de la responsabilité des fondateurs si les capitaux propres de départ sont manifestement insuffisants pour l'activité prévue pendant une période d'au moins deux ans et que la société fait faillite dans les 3 ans suivant sa constitution.
>
> Le(s) comparant(s) demande(nt) au notaire d'acter la constitution d'une société ayant les statuts suivants:
>
> ### Statuts
> 
> Art 1. La société a la forme d'une société à responsabilité limitée, se dénomme **[NOM: Speedol]** et est établie en région **[REGION: Bruxelloise]** <a name="2:8.2.1" href="#2:8.2.1-toc">(2:8 § 2 1°)</a>, <a name="2:8.2.2" href="#2:8.2.2-toc">(2:8 § 2 2°)</a>.
> 
> Art. 2. L'exercice social commence le 1er janvier et finira le 31 décembre de chaque année <a name="2:8.2.7" href="#2:8.2.7-toc">(2:8 § 2 7°)</a>.
> 
> Art. 3. L'assemblée générale décide de la manière dont le bénéfice annuel net est utilisé, sur la base d’une proposition de l'organe d'administration. <a name="2:8.2.8" href="#2:8.2.8-toc">(2:8 § 2 8°)</a>.
> 
> Art. 4. L'assemblée générale nomme le ou les administrateur(s) fixe leur nombre, la durée de leur mandat et leurs pouvoirs. Lorsque la loi l'exige, le contrôle de la société est assuré par un ou plusieurs commissaires, nommés conformément aux articles 3:88 et 3:89 du Code des sociétés <a name="2:8.2.9" href="#2:8.2.7-toc">(2:8 § 2 9°)</a>. Chaque administrateur - aussi lorsqu'il y en a plusieurs - représente la société vis-à-vis de tiers, ainsi qu'en justice, tant comme demandeur que comme défendeur. La société est en même temps engagée valablement par tout représentant désigné par procuration spéciale.
> 
> Art. 5. La société a pour objet toutes activités généralement quelconques se rapportant de près ou de loin, directement ou indirectement à l'informatique, la recherche, la conception, le développement, la technologie, la consultance, la fourniture de services ou prestations, la finance, la construction, l'immobilier, le nettoyage, la restauration en général et le secteur Horeca, la nourriture, l'événementiel, le transport, le commerce ambulant, la vente en gros et au détail, l'import-export, la location, la réparation, la fabrication, sans que cette liste soit exhaustive. Elle peut accomplir tous les actes et fonctions licites, au sens le plus large du terme. <a name="2:8.2.12" href="#2:8.2.12-toc">(2:8 § 2 12°)</a>
> 
> Art. 6. Il est tenu chaque année, au siège ou à l'endroit indiqué dans les convocations, une assemblée générale ordinaire le premier vendredi du mois de juin, à dix-huit heures. Tous les titulaires sont admis à l'assemblée générale mais seul les actionnaires peuvent y exercer le droit de vote <a name="2:8.2.13" href="#2:8.2.13-toc">(2:8 § 2 13°)</a>.
> 
> Art. 7. En rémuneration des apports, **[ACTIONS: huit cent quarante (840)]** actions ont été émises, qui en disposition contraire à l'articles 5:5 du Code des sociétés, ne doivent pas être libérées, l'administrateur décide souverainement des appels de fonds à effectuer par les titulaires d'actions non entièrement libérées <a name="5:3" href="#5:3-toc">(5:3)</a>, <a name="5:12.4" href="#5:12.4-toc">(5:12 4°)</a>, <a name="5:5" href="#5:5-toc">(5:5)</a>, <a name="5:8" href="#5:8-toc">(5:8)</a>.
>
> ### Dispositions finales et transitoires.
>
> Le(s) comparant(s) prend/prennent à l'unanimité les décisions suivantes qui ne deviendront effectives qu'à dater du dépôt au greffe d'une expédition de l'acte constitutif:
>
> L'adresse du siège est [**ADRESSE: rue du Labrador 26, 1000 Bruxelles**],
>
> Le premier exercice social commencera le jour de l'acquisition par la société de la personnalité morale et finira le 31 décembre de l'année suivante à cette acquisition.
>
> La nomination d'un administrateur non statutaire pour une durée illimitée: **[NOM1: Dupont Pierre]** <a name="2:8.2.10" href="#2:8.2.10-toc">(2:8 § 2 10°)</a>.
>
> Le montant total des frais qui incombent à la société à raison de sa constitution est approximativement de 457,30EUR <a name="5:12.7" href="#5:12.7-toc">(5:12 7°)</a>.
>
> Ce montant comprend entre autres le droit d'écriture s'élèvant à nonante-cinq euros (95,00 EUR), les droits d'enregistrement à cinquante (50EUR), les honoraires legaux du notaire à quarante-deux euros dix-huit centimes (42,18 EUR), les frais de publication au Moniteur belge à deux cent quarante et un euros vingt-sept cents (€ 241,27), la TVA et frais administratifs.
>
> Le(s) fondateur(s) déclare(nt) avoir reçu et lu en temps utile un projet du présent acte, et reconnaît (ssent) que le notaire a attiré son/leur attention sur le droit de (chacun d'eux) de désigner un autre notaire ou de se faire assister par un conseil, en particulier quand l'existence d'intérêts contradictoires ou d'engagements disproportionnés est constatée.
>
> Dont acte, fait et passé, date et lieu que dessus.
>
> Après, confirmation des identités du/des comparant(s), lecture partielle et commentaire complet de l'acte, le(s) comparant(s) a/ont signé avec le notaire.

Localiser un notaire disponible et fixer un rendez vous en ligne en allant sur <a href="https://www.notaire.be/notaire/recherchez/1000"/>la liste des notaires</a> en remplissant un code postale et selectionner parmis ceux qui ont l'option "Disponible pour rendez-vous en ligne", et qui ont des disponibilités. Dans les commentaires vous pouvez mentionner: <a href="https://www.ejustice.just.fgov.be/cgi_loi/change_lg_2.pl?language=fr&nm=1803031601&la=F">Art. 3. de la loi du 25 ventôse an XI.</a>

> Mon projet d'acte de constitution est complet, et vous a été communiqué via la plateforme startmybusiness. Je requiert donc l'exercice de votre ministère, au sens de l'art 3. de la loi du 25 ventôse de l'an XI lors du rendez-vous.

Ensuite remplissez les informations sur le site <a href="https://startmybusiness.be/">startmybusiness.be</a> en selectionnant le meme notaire, attention aux bugs suivants sur le site:

1. Problème des documents:

    Il faut uploader les documents via l'option "Documents / Ajoute un document" avant de remplir les autres formulaires sinon impossible de remplir les données financières.

    - La révision du projet d'acte (srl\_acte.docx)
    - L'attestation bancaire. Qui est ne devrait pas être requis mais qui l'est (srl\_banque.pdf)

    Donc pour cette derniere remplir un document vide stipulant:

    > <a href="srl_banque.docx" style="float: right;">⬇️  srl_banque.docx</a>
    > <br style="clear: right;">
    > Le capital sera libéré après la constitution, la société ne nécessite pas encore un compte auprès d'une institution bancaire.

2. Problème des actions:

    Dans montant des apports libérées, il est impossible de mettre 0. Donc mettre 1.

## 3. Inscription à la Banque-Carrefour des Entreprises (BCE)

Cout 90,50 EUR, à payer a un Guichet d'entreprise, reference légale <a href="http://www.ejustice.just.fgov.be/eli/loi/2019/03/23/2019A40586/justel">Code des societés Art. 2:6</a>.

Liste des <a href="https://economie.fgov.be/fr/themes/entreprises/creer-une-entreprise/demarches-pour-creer-une/demarches-aupres-dun-guichet">Guichets d'entrepise</a>.

Formulaire <a href="https://www.jelancemaboite.be/enregistrement_chez_securex"/>Securex</a> sans obligation de creation de compte, ne pas oublier de décocher le service optionel d'inscription TVA.

## 4. Demande d’identification à la TVA 

Formulaire en ligne <a href="http://eservices.minfin.fgov.be/VAT001/">Formulaire TVA 604A en ligne</a> source <a href="https://finances.belgium.be/fr/entreprises/tva/declaration/debut-fin-modification-activite#q1">SPF</a>.

## 5. Registre d'actionnaire.

Noter dans un registre d'actionnaire papier les participations de chaque actionnaire. Ensuite enregistrer les bénéficiaires dans le registre UBO.

## Frais et démarches recurrentes

Trimestrielles:

1. Cloture et déclations TVA.

Anuelles:

1. Cloture des comptes et assemblée générale.
2. Declaration Impôt des sociétés ISOC sur biztax.
2. Publication à la Banque nationnale BNB: 54,90 <a href="https://www.nbb.be/fr/centrale-des-bilans/deposer/paiement/frais-de-depot/tarifs-pour-societes-2021">Tarifs BNB 2021</a>
2. Cotisation sociale entreprise: 347,50 EUR <a href="https://www.inasti.be/fr/faq/quelle-cotisation-a-charge-des-societes-dois-je-payer">Insati</a>.

## Remerciement et License

Merci à

- Mathieu Michel, secrétaire d’État à la Digitalisation, chargé de la Simplification administrative.
- Paul Maselis, notaire à Bruxelles.

Pour les corrections ou propositions de simplification supplémentaires, n'hesitez pas à ouvrir une pull request sur <a href="https://github.com/antonylesuisse/belgium-srl">github</a>.

Domaine publique, Antony Lesuisse, 2021.
