# Payment Rails

A **funding platform** is the public page where a supporter chooses to help. A **payment processor** moves the money. A **payout rail** moves the balance to the maintainer. These layers can be owned by different companies.

| Rail | What it feels like to a supporter | Common constraint |
| --- | --- | --- |
| Card | Familiar checkout | International card and FX fees. |
| PayPal | Existing balance or saved account | Country, currency, and account restrictions. |
| Apple Pay / Google Pay | One-tap mobile checkout | Availability depends on checkout integration. |
| Bank transfer / invoice | Useful for companies | Too much friction for casual donors. |
| Crypto | Direct wallet payment | Volatility, custody, conversion, and tax complexity. |

The practical rule is simple: choose the public platform for the audience, then inspect the underlying processor and payout route for your country.
