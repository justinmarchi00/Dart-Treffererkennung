export default function PlayerCard({ player, active }) {

    return (

        <div
            className={`rounded-[35px] p-8 border-2 ${
                active
                    ? 'bg-[#101010] border-[#00ff99]'
                    : 'bg-[#101010] border-[#1f1f1f]'
            }`}
        >

            <div className="flex justify-between">

                <div>

                    <div className="flex items-center gap-3 mb-3">

                        <h2 className="text-4xl font-black">
                            {player.name}
                        </h2>

                        {active && (
                            <span className="bg-[#00ff99] text-black px-3 py-1 rounded-full text-xs font-black">
                                AM ZUG
                            </span>
                        )}

                    </div>

                    <div className="text-[90px] font-black">
                        {player.score}
                    </div>

                </div>

                <div className="text-right">

                    <div className="text-zinc-500 mb-2">
                        Checkout
                    </div>

                    <div className="text-4xl font-black text-[#00ff99]">
                        {player.checkout}
                    </div>

                </div>

            </div>

            <div className="grid grid-cols-3 gap-4 mt-8">

                {player.darts.map((dart, i) => (

                    <div
                        key={i}
                        className="bg-[#181818] rounded-2xl p-5 text-center text-3xl font-black"
                    >
                        {dart}
                    </div>

                ))}

            </div>

            <div className="mt-6 text-zinc-500">
                Dart {player.currentDart}/3
            </div>

        </div>
    )
}